# Data Type Conversion in Python
# In Python, you can convert between different data types using built-in functions.
# Here are some common data type conversion functions:

# Convert to integer
# 1. float to integer
float_val = 5.0
int_val = int(float_val)  # Convert float to integer
print(int_val)  # Output: 5
# 2. string to integer
str_val = "5"
int_val = int(str_val)  # Convert string to integer
print(int_val)  # Output: 5
# 3. boolean to integer
bool_val = True
int_val = int(bool_val)  # Convert boolean to integer
print(int_val)  # Output: 1

# Convert to float
# 1. integer to float
int_val = 5
float_val = float(int_val)  # Convert integer to float
print(float_val)  # Output: 5.0
# 2. string to float
str_val = "5.0"
float_val = float(str_val)  # Convert string to float
print(float_val)  # Output: 5.0
# 3. boolean to float
bool_val = True
float_val = float(bool_val)  # Convert boolean to float
print(float_val)  # Output: 1.0

# Convert to string
# 1. integer to string
int_val = 5
str_val = str(int_val)  # Convert integer to string
print(str_val)  # Output: "5"
# 2. float to string
float_val = 5.0
str_val = str(float_val)  # Convert float to string
print(str_val)  # Output: "5.0"
# 3. boolean to string
bool_val = True
str_val = str(bool_val)  # Convert boolean to string
print(str_val)  # Output: "True"

# Convert to boolean
# 1. integer to boolean
int_val = 0
bool_val = bool(int_val)  # Convert integer to boolean
print(bool_val)  # Output: False
# 2. float to boolean
float_val = 0.0
bool_val = bool(float_val)  # Convert float to boolean
print(bool_val)  # Output: False
# 3. string to boolean
str_val = ""
bool_val = bool(str_val)  # Convert string to boolean
print(bool_val)  # Output: False
