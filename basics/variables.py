name = "Vivek"
age = 32
print(name)
print(age)

# Single line comment

"""
Multi-line comment
"""

age = 33
print(age)  # updating the value of age variable
# age = "thirty three"
print(type(age))
# this will work but it is not recommended to change the data type of a variable

"""
Supported variable names:
- Can contain letters, numbers, and underscores
    e.g., 'name', 'age', 'first_name', 'age_32'
- Cannot start with a number
    e.g., '32' is not a valid variable name
- Cannot be a reserved keyword 
    e.g., like 'if', 'for', 'while'
- Should be descriptive of the value it holds 
    e.g., 'age', 'name', 'is_student'
- Should not contain spaces (use underscores instead)
    e.g., 'first_name'
- Variable names are case-sensitive 
    e.g., 'age' and 'Age' are different variables
- Avoid using special characters in variable names
    e.g., '@', '#', '$'
- Avoid using single-character variable names unless they are used in a specific context (like in loops or mathematical operations)
    e.g., 'x', 'y', 'z'
- Use lowercase letters for variable names  to follow Python's naming conventions
    e.g., 'age', 'name', 'is_student'


Python naming conventions:
- Use lowercase letters for variable names (e.g., 'age', 'name', 'is_student')
- Use uppercase letters for constants (e.g., 'PI', 'SPEED_OF_LIGHT')
- Use CamelCase for class names (e.g., 'Person', 'Car', 'Animal')
- Use snake_case for function and variable names (e.g., 'calculate_area', 'first_name')
- Avoid using single-character variable names unless they are used in a specific context (like in loops or mathematical operations) (e.g., 'x', 'y', 'z')
- Use descriptive names for variables, functions, and classes to improve code readability (e.g., 'calculate_area' instead of 'ca')
"""

"""
Variable vs identifier

# A variable is a container that holds a value. 
# It can be changed during the execution of the program.
# An identifier is the name used to identify a variable, function, class, module, or other object in Python. 
# It is a name that you give to a variable, function, class, module, or other object in your code. 
"""


# inline variable assignment with same values
a = b = c = 1
print(a, b, c)

# inline variable assignment with different values
x, y, z = 1, 2, 3
print(x, y, z)

# different data types in a single line
name_string, age_int, amount_float, is_student_bool = "Alice", 25, 100.50, True
print(name_string, age_int, amount_float, is_student_bool)

# variable assignment with expressions
a = 10
b = 20
c = a + b
print(c)
