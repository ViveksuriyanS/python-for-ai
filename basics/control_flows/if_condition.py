
# If-elif-else statements in Python
# Used for conditional execution of code blocks based on certain conditions

temp = 29
if temp > 30:
    print("It's a hot day.")
elif temp > 20:
    print("It's a nice day.")
else:
    print("It's a cold day.")


# Example with multiple conditions
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

# Example with nested if statements
num = 10
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")    
