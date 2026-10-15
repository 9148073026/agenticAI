import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

similarity = np.dot(vector_a, vector_b) / (
    np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
)

print(similarity)