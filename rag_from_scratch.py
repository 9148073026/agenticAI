import os
import json
from anyio import Path
from openai import OpenAI
from dotenv import load_dotenv
import chromadb

print("Starting the RAG from scratch script...")
print("imported all necessary packages")

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Placeholder; local Ollama needs no real key
)

print("Ollama client initialized")

# Load plain-text documents
data_dir = Path(r"S:\AI\dataset")

def read_document(filename):
    filepath = rf"S:\AI\dataset\{filename}"

    with open(filepath, "r", encoding="utf-8-sig") as file:
        return file.read()
    


hr_policy = read_document("company_hr_policy.txt")
eng_doc = read_document("engineering_standards.txt")
onboarding_guide = read_document("onboarding_guide.txt")
product_knowledge = read_document("product_knowledge_base.txt")
sec_policy = read_document("security_policy.txt")


print("All five documents loaded successfully.")

# Test local text generation
response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": (
                "Explain Retrieval-Augmented Generation (RAG) "
                "in large language models using a banking example."
            ),
        }
    ],
)

#print(response.choices[0].message.content)

#print(response.model_dump_json(indent=2))

#print(hr_policy[:200])
#print(sec_policy[:10000])

print("length of hr_policy:", len(hr_policy))
print("split length of hr_policy:", len(hr_policy.split()))
print("length of sec_policy:", len(sec_policy))
print("split length of sec_policy:", len(sec_policy.split()))
print("length of eng_doc:", len(eng_doc))
print("split length of eng_doc:", len(eng_doc.split()))
print("length of onboarding_guide:", len(onboarding_guide))
print("split length of onboarding_guide:", len(onboarding_guide.split()))
print("length of product_knowledge:", len(product_knowledge))
print("split length of product_knowledge:", len(product_knowledge.split()))

def chunk_document(text, source_name):
    """
    Split a document into chunks by paragraph.
    Returns a list of dicts with text and metadata.
    """
    # Split on double newlines
    paragraphs = text.strip().split("\n\n")

    chunks = []
    for para in paragraphs:
        para = para.strip()
        # Skip short lines (headers, separators)
        if len(para) < 50:
            continue
        # Skip separator lines
        if para.startswith("===="):
            continue
        chunks.append({
            "text": para,
            "source": source_name
        })

    return chunks

hr_chunks = chunk_document(hr_policy, "HR Policy")
engineering_chunks = chunk_document(eng_doc, "Engineering")
onboarding_chunks = chunk_document(onboarding_guide, "Onboarding")
product_chunks = chunk_document(product_knowledge, "Product")
security_chunks = chunk_document(sec_policy, "Security")

all_chunks = (
    hr_chunks
    + engineering_chunks
    + onboarding_chunks
    + product_chunks
    + security_chunks
)

print(len(hr_chunks))

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = ''' Office Network:
- Connect only to the "NovaTech-Secure" WiFi network (WPA3)
- The "NovaTech-Guest" network is for visitors only — employees should not use it
- Do not connect personal IoT devices (smart speakers, etc.) to the office network '''

embeddings = model.encode(sentences)

print(embeddings.shape)
print(embeddings)


sentence1 = ''' I love chicken Biriyani '''
sentence2 = ''' I love eating flaovured rice with chicken'''
sentence3 = ''' I am doing work from Home'''

embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)
embedding3 = model.encode(sentence3)

print(embedding1.shape)
print(embedding2.shape)
print(embedding3.shape)

#storing chunks with chroma db

chroma_clinet = chromadb.Client()
collection = chroma_clinet.create_collection(name="company_docs")

documents = []
ids = []
metadatas = []

for i, chunk in enumerate(all_chunks):
  documents.append(chunk['text'])
  ids.append(f"chunk_{i}")
  metadatas.append({"source": chunk["source"]})

print(documents[110])
print(ids[110])
print(metadatas[110])

collection.add(
    documents = documents,
    ids = ids,
    metadatas = metadatas
)

print(f" Stored {len(documents)} chunks in chroma db")
print(f" Sources: 5 differnt files")