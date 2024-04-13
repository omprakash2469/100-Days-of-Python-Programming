"""
dir()
--
The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
"""
x = [1, 2, 3, 4]
print(dir(x)) # Returns list of all atrributes and methods


"""
__dict__
---
The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.__dict__) # Returns a dictionary representation of an object's attributes



"""
help()
---
The help() function is used to get help documentation for an object, including a description of its attributes and methods.
"""

print(help(list))