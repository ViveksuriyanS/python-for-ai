# The input() function is used to take input from the user.
# The input is taken as a string.
# So if you want to use it as a number, you need to convert it to the appropriate type
# (e.g., int for integers).

inputFromUser = input("Enter a number: ")
number = int(inputFromUser)  # Convert the input string to an integer
print(
    "You entered the number: " + str(number)
)  # Convert the number back to a string for concatenation in the print statement
