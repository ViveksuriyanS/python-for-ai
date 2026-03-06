# Random Package

# Pattern 1: Importing the entire random package
import random
# Example usage of random package
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_integer}") # Output: Random integer between 1 and 10: 7 (example output)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}") # Output: Random float between 0 and 1: 0.543210987654321 (example output


# Pattern 2: Importing specific functions from the random package
from random import randint, choice
# Example usage of imported functions
# Generate a random integer between 1 and 10
random_integer = randint(1, 10)
print(f"Random integer between 1 and 10: {random_integer}") # Output:

# Generate a random choice from a list
options = ['apple', 'banana', 'cherry']
random_choice = choice(options)
print(f"Random choice from the list: {random_choice}") # Output: Random choice from the list: banana (example output)

