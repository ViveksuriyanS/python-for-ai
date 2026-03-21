# Example of class inheritance in Python
# Inheritance allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). 
# This promotes code reusability and can make it easier to create and maintain applications.

# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."

# Derived class (child class) that inherits from the Animal class
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!" 


Animal1 = Animal("Generic Animal")
print(Animal1.eat())

Dog1 = Dog("Buddy")
print(Dog1.eat())  # Inherited method from Animal class
print(Dog1.bark())  # Method specific to Dog class
print(Dog1.sleep())  # Inherited method from Animal class