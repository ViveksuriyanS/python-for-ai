class Animals:
    def __init__(self, name):
        self.name = name
    
class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed  # Add a new attribute specific to the Dog class

# Create an instance of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
print(f"Name: {dog1.name}, Breed: {dog1.breed}")

# Create another instance of the Dog class with named arguments
dog2 = Dog(name="Max", breed="Labrador")
print(f"Name: {dog2.name}, Breed: {dog2.breed}")    

