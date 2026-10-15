numbers = [1, 2, 3, 4, 5,8]
print(numbers)  
even_numbers = {}

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")  
        even_numbers[number] = number*number

print(even_numbers)

##make a dictionary that maps each word to its length, but includes 
# only words longer than 3 characters. Try a loop first.
words = ["cat", "elephant", "dog", "butterfly"]
word_lengths = {}

for word in words:
    if len(word) > 3:
        word_lengths[word] = len(word)


print(word_lengths)

##dictionary comprehension
word_lengths = {word: len(word) for word in words if len(word) > 3}
print(word_lengths)
