# For loop is used to iterate over a sequence
#   (like a list, tuple, string, etc.) or other iterable objects.
# Allows you to execute a block of code repeatedly for each item in the sequence.


# E.g., Iterating over a list
list = [1, 2, 3, 4, 5]
for listItem in list:
    print(listItem)

# E.g., Iterating over a string
string = "Hello"
for chars in string:
    print(chars)

# E.g., Iterating over a range of numbers [From 0 to 4]
for i in range(5):
    print(i)

# prints from 1 to 5 [before 6]
for i in range(1, 6):
    print(i)

# Prints from 1 to 9 with a step of 2
for i in range(1, 10, 2):
    print(i)

# Prints from 10 to 1 in reverse order [-1]
for i in range(10, 0, -1):
    print(i)
