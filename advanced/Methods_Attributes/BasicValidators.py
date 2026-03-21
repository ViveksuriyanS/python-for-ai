class DataValidator:
    def __init__(self):
        self.errors = []
    
    # Method to validate if the data is a non-empty string
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age:{age}")
            return False
        return True
    
    # Method to validate if the email is correctly formatted
    def validate_email(self, email):
        if "@" not in email or "." not in email:
            self.errors.append(f"Invalid email:{email}")
            return False
        return True
    
    # Method to print all the errors
    def print_errors(self):
        if self.errors:
            print("Errors Found:")
            for error in self.errors:
                print(error)
        else:
            print("No errors found.")

    # Return errors
    def get_errors(self):
        return self.errors
    
# Example usage
validate = DataValidator()
ageValidate = validate.validate_age(525)
age1Validate = validate.validate_age(age = 25)
emailValidate = validate.validate_email("v@v.c")
email1Validate = validate.validate_email(email = "bademail.com")
validate.print_errors()
validate.get_errors()
