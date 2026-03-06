# Tuples in Python
# A tuple is a collection of items that are ordered and $$ unchangeable $$.
# Tuples are defined by enclosing the items in parentheses () and separating them with commas.
# Example of a tuple
coordinates = (1, 2, 3)
print(coordinates) # Output: (1, 2, 3)

# Accessing tuple items
print(coordinates[0]) # Output: 1
print(coordinates[1]) # Output: 2
print(coordinates[2]) # Output: 3

# Tuples are immutable, so you cannot modify their items
# coordinates[0] = 10 # This will raise an error

# Tuple methods
print(len(coordinates)) # Output: 3
print(coordinates.count(1)) # Output: 1
print(coordinates.index(2)) # Output: 1