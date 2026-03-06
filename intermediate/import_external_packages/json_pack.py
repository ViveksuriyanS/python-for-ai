# JSON Package

# Pattern 1: Importing the entire json package
import json
# Example usage of json package
# Convert a Python dictionary to a JSON string
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}") # Output: JSON string: {"name":
# Convert a JSON string back to a Python dictionary
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(f"Python dictionary: {data}") # Output: Python dictionary: {'name': 'John', 'age': 30, 'city': 'New York'}

# Pattern 2: Importing specific functions from the json package
from json import dumps, loads
# Example usage of imported functions
# Convert a Python dictionary to a JSON string
data = {"name": "Jane", "age": 25, "city": "Los Angeles"}
json_string = dumps(data)
print(f"JSON string: {json_string}") # Output: JSON string: {"name": "Jane", "age": 25, "city": "Los Angeles"}
# Convert a JSON string back to a Python dictionary
json_string = '{"name": "Jane", "age": 25, "city": "Los Angeles"}'
data = loads(json_string)
print(f"Python dictionary: {data}") # Output: Python dictionary: {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'} 
