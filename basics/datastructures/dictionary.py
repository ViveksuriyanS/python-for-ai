# Dictionaries in Python
# A dictionary is a collection of key-value pairs that are unordered and changeable.
# Dictionaries are defined by enclosing the key-value pairs in curly braces {} and separating them with commas.
# Example of a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing dictionary values
print(person["name"]) # Output: Alice
print(person["age"]) # Output: 30
print(person["city"]) # Output: New York

# Modifying dictionary values
person["age"] = 31
print(person) # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding items to a dictionary
person["email"] = "alice@example.com"
print(person) # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Removing items from a dictionary [del, pop]
del person["city"]
print(person) # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}
popped_email = person.pop("email")
print(popped_email) # Output: alice@example.com
print(person) # Output: {'name': 'Alice', 'age': 31}

# Dictionary methods
print(len(person)) # Output: 2
print(list(person.keys())) # Output: ['name', 'age']
print(list(person.values())) # Output: ['Alice', 31]
print(list(person.items())) # Output: [('name', 'Alice'), ('age', 31)]