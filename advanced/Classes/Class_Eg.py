class TestVivek:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def TestQuality(self, clear=True, anger=True, happy=True):
        self.clear = clear
        self.anger = anger
        self.happy = happy
        if self.clear and self.anger and self.happy:
            print(clear, anger, happy)
            return "Vivek is a good person"
        else:
            return "Vivek is not a good person"

# Creating an object of the class TestVivek
object1 = TestVivek("Viveksuriyan", "Subramani")
print(object1.firstname + " " + object1.lastname)

# Calling the method TestQuality
result = object1.TestQuality(False, False)
print(result)

