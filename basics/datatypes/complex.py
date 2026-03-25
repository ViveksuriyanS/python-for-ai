# Complex Numbers in Python
# A complex number is a number that has a real part and an imaginary part.
# In Python, complex numbers are represented using the 'complex' data type.
# The real part is represented by the 'real' attribute, and the imaginary part is represented by the 'imag' attribute.
# You can create a complex number using the 'complex()' function or by using the 'j' suffix for the imaginary part.
# Example of creating complex numbers
complex_num1 = complex(
    2, 3
)  # Creates a complex number with real part 2 and imaginary part 3
complex_num2 = 4 + 5j  # Creates a complex number with real part 4 and imaginary part 5
print(complex_num1)  # Output: (2+3j)
print(complex_num2)  # Output: (4+5j)
print(type(complex_num1))  # Output: <class 'complex'>
print(type(complex_num2))  # Output: <class 'complex'>
