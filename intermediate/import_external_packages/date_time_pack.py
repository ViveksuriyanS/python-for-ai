# Date and Time Package

# Pattern 1: Importing the entire datetime package
import datetime
# Example usage of datetime package
# Get the current date and time
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}") # Output: Current date and time

# Get the current date
current_date = datetime.date.today()
print(f"Current date: {current_date}") # Output: Current date
# Pattern 2: Importing specific classes from the datetime package
from datetime import datetime, date
# Example usage of imported classes
# Get the current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}") # Output: Current date and time

# Get the current date
current_date = date.today()
print(f"Current date: {current_date}") # Output: Current date
