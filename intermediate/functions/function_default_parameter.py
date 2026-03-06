def print_full_name(first_name="Vivek", last_name="Smith"):
    full_name = f"{first_name} {last_name}"
    print(full_name)

print_full_name("John") # Output: John Smith
print_full_name("Jane", "Doe") # Output: Jane Doe
print_full_name() # Output: Vivek Smith
print_full_name(last_name="Johnson") # Output: Vivek Johnson
print_full_name(first_name="Emily") # Output: Emily Smith   