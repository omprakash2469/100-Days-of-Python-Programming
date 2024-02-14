"""
Types of errors
---

IndexError      =   When the wrong index of a list is retrieved.
AssertionError  =   It occurs when the assert statement fails
AttributeError  =   It occurs when an attribute assignment is failed.
ImportError     =   It occurs when an imported module is not found.
KeyError        =   It occurs when the key of the dictionary is not found.
NameError       =   It occurs when the variable is not defined.
MemoryError     =   It occurs when a program runs out of memory.
TypeError       =   It occurs when a function and operation are applied in an incorrect type.
"""


# Exception handling
num = input("Enter a number: ")

try:
    num = int(num)
    print(f"Multiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
except ValueError:
    print("Invalid input! Please enter an integer")