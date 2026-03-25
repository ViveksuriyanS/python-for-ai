intVal = 100
boolVal = True
strVal = "Hello, World!"
floatVal = 3.14

# Print the values and the address of the variables
print("Integer value: {i}, Address: {a}".format(i=intVal, a=id(intVal)))
print("Boolean value: {b}, Address: {a}".format(b=boolVal, a=id(boolVal)))
print("String value: {s}, Address: {a}".format(s=strVal, a=id(strVal)))
print("Float value: {f}, Address: {a}".format(f=floatVal, a=id(floatVal)))

"""
Output:
Integer value: 100, Address: 140703353388432
Boolean value: True, Address: 140703353388432
String value: Hello, World!, Address: 140703353388432
Float value: 3.14, Address: 140703353388432
"""
