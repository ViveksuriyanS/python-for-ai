# Strings in Python
# A string is a sequence of Unicode characters
# enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning they cannot be changed after they are created.


long_dash = "—" * 20
print(long_dash)  # Output: ————————————————————
length = len(long_dash)
print(length)  # Output: 20


# Concatenation of strings
first_name = "Viveksuriyan"
last_name = "Subramani"
age = "32"
description = """
    Viveksuriyan Subramani is a software engineer with expertise in Python programming and AI development.
    He has a strong background in machine learning, deep learning, and natural language processing.
    Viveksuriyan is passionate about creating innovative solutions and has a proven track record of delivering high-quality software products.
    He is a dedicated professional who continuously seeks to expand his knowledge and skills in the field of artificial intelligence.
"""
full_name = first_name + " " + last_name
print(full_name)  # Output: Viveksuriyan Subramani
print(
    description
)  # Output: Viveksuriyan Subramani is a software engineer with expertise in Python programming and AI development. He has a strong background in machine learning, deep learning, and natural language processing. Viveksuriyan is passionate about creating innovative solutions and has a proven track record of delivering high-quality software products. He is a dedicated professional who continuously seeks to expand his knowledge and skills in the field of artificial intelligence.

# f-strings for string interpolation
age = 32
greeting = f"Hello, my name is {full_name} and I am {age} years old."
print(
    greeting
)  # Output: Hello, my name is Viveksuriyan Subramani and I am 32 years old.

# String methods

# Convert the string to uppercase, lowercase, title case
print(full_name.upper())  # Output: VIVEKSURIYAN SUBRAMANI
print(full_name.lower())  # Output: viveksuriyan subramani
print(full_name.title())  # Output: Viveksuriyan Subramani
print(full_name.split())  # Output: ['Viveksuriyan', 'Subramani']

# Split the string into a list of words, and replace a substring with another substring
print(type(full_name.split()))  # Output: <class 'list'>
print(full_name.replace("Viveksuriyan", "Vivek"))  # Output: Vivek Subramani

# Checking if a string starts with or ends with a specific substring
print(full_name.startswith("Vivek"))  # Output: True
print(full_name.endswith("Subramani"))  # Output: True
print("Vivek" in full_name)  # Output: True

# Stripping whitespace from the beginning and end of a string
txt = "   Hello, World!   "
print(txt.strip())  # Output: Hello, World!
print(txt.lstrip())  # Output: Hello, World!
print(txt.rstrip())  # Output:    Hello, World!

print(txt.find("World"))  # Output: 10
print(txt.count("o"))  # Output: 2
