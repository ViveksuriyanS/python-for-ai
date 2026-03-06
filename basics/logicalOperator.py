age = 25
has_license = True

# Logical operators

# AND operator - returns True if both conditions are True
can_drive = age >= 18 and has_license
print(can_drive) # Output: True


# OR operator - returns True if at least one condition is True
is_weekend = False
can_go_out = can_drive or is_weekend
print(can_go_out) # Output: True

# NOT operator - returns True if the condition is False
is_raining = True
should_take_umbrella = is_raining and can_go_out
print(should_take_umbrella) # Output: True
