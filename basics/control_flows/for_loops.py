# For loops in Python
# Used for iterating over a sequence (like a list, tuple, string) or other iterable objects
# Example with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example with a string
for char in "Hello":
    print(char)

# Example with a range of numbers
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

# Example with a range of numbers with a step
for i in range(0, 10, 2):
    print(i) #

# Example with nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Example with an if condition inside a for loop
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.") 
# Output: 1 is odd, 2 is even, 3 is odd, 4 is even, 5 is odd


# Example with a for loop and a list of dictionaries
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19}
]
for student in students:
    print(f"{student['name']} is {student['age']} years old.")
# Output: Alice is 20 years old, Bob is 22 years old, Charlie is 19 years old   


