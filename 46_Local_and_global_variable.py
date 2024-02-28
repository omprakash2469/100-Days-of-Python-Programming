# Local and Global variable
"""
What is a variable ?
---
A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator ( = )


Local Variable
---
A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.


Global Variable 
---
A global variable is a variable that is defined outside of a function and is accessible from within any function in your code.
"""

a = 5

def hello():
    # a = 20
    # global a # Change global variable inside of a function
    a = 20
    y = 12
    print(a) # Access global variable
    
    print("These are fruits")
    

hello()
print(a)
# print(y) # cannot access local variable outside of a function
