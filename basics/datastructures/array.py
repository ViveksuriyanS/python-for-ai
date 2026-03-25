name = "Viveksuriyan"

# Name is a array of characters
# The index starts from 0 to n-1 where n is the length of the array
print(name[1])

# We can also use negative indexing to access elements from the end of the array
print(name[-1])  # This will print the last character 'n'
print(name[len(name) - 1])  # This will also print the last character 'n'

# We can also use slicing to access a range of characters in the array
# Syntax: array[start:end] - Return start to end - 1
print(name[0:6])  # This will print 'Viveks'

# We can also use slicing with a step to access every nth character in the array
# Syntax: array[start:end:step] - Return start to end - 1 with a step of step
print(name[0:11:2])  # This will print 'Viksrn'

# We can also use slicing to access characters from the mid of the array
# Syntax: array[start:] - Return start to end - 1
print(name[6:])  # This will print 'suriyan' - from index 6 to the end of the array


print(name[::])  # This will print the entire array 'Viveksuriyan'

# We can also use slicing to access characters from end of the array
print(name[::-1])  # This will print the array in reverse order 'nayiruskiveV'


# Other cases
print(name[-1:-3:-1])  # This will print 'na' - from index -1 to -3 with a step of -1

print(name[:-3:-1])  # This will print 'na'

print(name[:-3:1])  # This will print 'Viveksuri' - from index 0 to -3 with a step of 1

print(name[:-3:])  # This will print 'Viveksuri' - from index 0 to -3 with a step of 1
