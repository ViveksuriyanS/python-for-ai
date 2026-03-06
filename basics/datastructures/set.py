# Sets in Python
# A set is a collection of unique items that are unordered and changeable.
# Sets are defined by enclosing the items in curly braces {} and separating them with commas.
# Example of a set
empty_set = set()
print(empty_set) # Output: set()
empty_set.add(1)
empty_set.add(1) # Adding a duplicate item will not change the set
empty_set.add(2)
print(empty_set) # Output: {1}

numbers = {1, 2, 3, 4, 5} # Initializing a set with multiple items
print(numbers) # Output: {1, 2, 3, 4, 5}

# Adding items to a set
numbers.add(6)
print(numbers) # Output: {1, 2, 3, 4, 5, 6}

# Removing items from a set
numbers.remove(3) # Raises an error if the item is not found
print(numbers) # Output: {1, 2, 4, 5, 6}

# Disacarding an item from a set (does not raise an error if the item is not found)
numbers.discard(10) # No error, since 10 is not in the set
print(numbers) # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # Output: {3}
print(set1.difference(set2)) # Output: {1, 2}

# Converting a list to set to remove duplicates
my_list = [1,2,3,4,5,1,2]
my_set = set(my_list)
print(my_set) # Output: {1, 2, 3, 4, 5}

# Convert a list of multiple data types to a set
mixed_list = [1, "hello", 3.14, True, 1, "hello"]
mixed_set = set(mixed_list)
print(mixed_set) # Output: {1, 'hello', 3.14, True} (order may vary)    