# Lists in Python
# A list is a collection of items that are ordered and changeable.
# Lists are defined by enclosing the items in square brackets [] and separating them with commas.
# Example of a list of integers
from itertools import count


numbers = [1, 2, 3, 4, 5]
print(numbers) # Output: [1, 2, 3, 4, 5]

# Example of a list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Example of a list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(mixed_list) # Output: [1, 'hello', 3.14, True]

# Accessing list items
print(numbers[0]) # Output: 1
print(fruits[1]) # Output: banana
print(mixed_list[2]) # Output: 3.14
print(mixed_list[-1]) # Output: True (negative indexing starts from the end of the list)

# Modifying list items
numbers[0] = 10
print(numbers) # Output: [10, 2, 3, 4, 5]

# Adding items to a list [append, insert]
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange'] 
fruits.insert(1, "blueberry")
print(fruits) # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange']

# Removing items from a list [remove, del, pop]
fruits.remove("banana")
print(fruits) # Output: ['apple', 'cherry', 'orange'] 
del fruits[0]  
print(fruits) # Output: ['cherry', 'orange']
popped_fruit = fruits.pop(0)
print(popped_fruit) # Output: cherry
print(fruits) # Output: ['orange']  

# List slicing
print(numbers[1:4]) # Output: [2, 3, 4]
print(fruits[:2]) # Output: ['apple', 'cherry']
print(mixed_list[1:]) # Output: ['hello', 3.14, True]

# List methods
print(len(numbers)) # Output: 5
print(numbers.count(1)) # Output: 0 (since we modified the first element to 10)
print(numbers.index(3)) # Output: 2 (index of the first occurrence of 3)
print(max(numbers)) # Output: 10
print(min(numbers)) # Output: 2
print(sum(numbers)) # Output: 24
print(sorted(numbers)) # Output: [2, 3, 4, 5, 10]
print(sorted(fruits)) # Output: ['apple', 'cherry', 'orange']   
print(numbers)
numbers.reverse()
print(numbers) # Output: [5, 4, 3, 2, 10]
