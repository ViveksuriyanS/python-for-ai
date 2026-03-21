
# This class calculates the area of a circle given its radius.
class AreaFindCircle:
    def __init__(self, radius): # Constructor to initialize the radius
        self.radius = radius

    def calculate_area(self): # Method to calculate the area of the circle
        import math
        return math.pi * (self.radius ** 2) 
    
# This class calculates the area of a rectangle given its length and width.
class AreaFindRectangle:
    def __init__(self, length, width): # Constructor to initialize the length and width
        self.length = length
        self.width = width

    def calculate_area(self): # Method to calculate the area of the rectangle
        return self.length * self.width

# This class calculates the area of a triangle given its base and height.
class AreaFindTriangle:
    def __init__(self, base, height): # Constructor to initialize the base and height
        self.base = base
        self.height = height

    def calculate_area(self): # Method to calculate the area of the triangle
        return 0.5 * self.base * self.height

# Example usage:
circle = AreaFindCircle(radius=5)
print(f"Area of Circle: {circle.calculate_area()}")

rectangle = AreaFindRectangle(length=4, width=6)
print(f"Area of Rectangle: {rectangle.calculate_area()}")

triangle = AreaFindTriangle(base=3, height=4)
print(f"Area of Triangle: {triangle.calculate_area()}")


