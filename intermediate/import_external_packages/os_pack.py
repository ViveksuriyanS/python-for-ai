# OS Package
# Pattern 1: Importing the entire os package
import os
# Example usage of os package
# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}") # Output: Current working directory: /
# List all files and directories in the current directory
files_and_directories = os.listdir()
print(f"Files and directories in the current directory: {files_and_directories}") # Output

# Pattern 2: Importing specific functions from the os package
from os import getcwd, listdir
# Example usage of imported functions
# Get the current working directory
current_directory = getcwd()
print(f"Current working directory: {current_directory}") # Output: Current working directory: /
# List all files and directories in the current directory
files_and_directories = listdir()
print(f"Files and directories in the current directory: {files_and_directories}") # Output
