# Function with return statement
# In Python, you can use the `return` statement to send a value back from a function.
# The `return` statement allows you to capture the output of a function and use it elsewhere in your code.
# Here's an example of a function that checks the weather based on the temperature and returns a message:
def check_weather(temp):
    if temp > 30:
        return "It's hot outside!"
    elif temp < 10:
        return "It's cold outside!"
    else:
        return "The weather is moderate."
    
# You can call the function and store the returned value in a variable
weather_message = check_weather(35)
print(weather_message) # Output: It's hot outside!

# Another example of a function that checks the area of a rectangle and returns the result:
def calculate_area(length, width):
    area = length * width
    return area
# Example usage
rect_area = calculate_area(5, 3)
print(rect_area) # Output: 15

# multiple return statements
# A function can have multiple return statements, allowing you to return different values based on certain conditions
def is_all_rounder(can_bat, can_bowl, can_field):
    if can_bat and can_bowl and can_field:
        return "All-rounder"
    else:
        return "Not an all-rounder"
    
# Example usage
player1 = is_all_rounder(True, True, True)
print(player1) # Output: All-rounder
player2 = is_all_rounder(True, False, True)
print(player2) # Output: Not an all-rounder     