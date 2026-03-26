# print a string
print("Hello")

# print variables
x = 10
y = 11
print("The value of x is ", x, " and y is ", y)

# another way to print using string.format() with positional arguments
print("The value of x is {} and y is {}".format(x, y))

# using format another version of string.format() with index position of arguments
print("The value of x is {0} and y is {1}".format(x, y))

# using temporary variables in string.format() with keyword arguments
print("The value of x is {num1} and y is {num2}".format(num1=x, num2=y))
