# Example of method overriding in Python

# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."
    
# Derived class (child class) that overrides the speak method
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class (child class) that overrides the speak method
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create an instance of the Dog class
dog1 = Dog("Buddy")
print(dog1.speak())  # This will call the overridden speak method in the Dog

# Create another instance of the Dog class
cat1 = Cat("Whiskers")
print(cat1.speak())  # This will call the overridden speak method in the Cat
