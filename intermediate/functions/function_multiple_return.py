# Function with multiple return values
# In Python, a function can return multiple values using tuples.
# This allows you to return more than one piece of information from a function.
# Here's an example of a function that calculates the area and perimeter of a rectangle and returns both
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example usage
rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"Area: {rect_area}, Perimeter: {rect_perimeter}") # Output: Area: 15, Perimeter: 16


