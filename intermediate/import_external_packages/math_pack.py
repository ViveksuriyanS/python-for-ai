# What is a package in Python?
# A package in Python is a way to organize related modules and functions into a single directory.
# It allows you to group related code together and makes it easier to manage and reuse.
# A package can contain multiple modules, which are simply Python files that contain functions, classes, and variables. 
# By using packages, you can create a structured and organized codebase, making it easier to maintain and understand.
# To create a package, you need to create a directory and include an __init__.py file inside it. The __init__.py file can be empty or contain initialization code for the package.
# Once you have a package, you can import it in your Python code and use the functions and classes defined in the modules within the package. This allows you to reuse code across different projects and promotes code modularity.


# Math Package

# Pattern 1: Importing the entire math package
import math
# Example usage of math package
# Calculate the square root of a number
number = 16
sqrt_number = math.sqrt(number)
print(f"The square root of {number} is {sqrt_number}") # Output: The square

# Calculate the power of a number
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}") # Output: 2 raised to the power of 3 is 8.0

# Pattern 2: Importing specific functions from the math package
from math import sqrt, pow
# Example usage of imported functions
# Calculate the square root of a number
number = 25
sqrt_number = sqrt(number)
print(f"The square root of {number} is {sqrt_number}") # Output: The square

# Calculate the power of a number
base = 2
exponent = 3
power_result = pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}") # Output: 2 raised to the power of 3 is 8.0