x = 3
# Try replacing the value 3 with 0 to see how the error handling works
try:
    result = 10 / x
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

