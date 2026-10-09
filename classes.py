class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.name)    # Buddy
print(dog.bark())  # Buddy says woof!

other_dog = Dog("Pluto")
print(other_dog.name)    # Pluto
print(other_dog.bark())  # Pluto says woof! 

other_dog.name = "puppy"
print(other_dog.name)    # Max
print(other_dog.bark())

def count_up(limit):
    i=0
    while i < limit:
        yield i 
        i = i+1

print(list(count_up(5)))  # [0, 1, 2, 3, 4]
