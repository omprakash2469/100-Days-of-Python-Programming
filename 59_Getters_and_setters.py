"""
Getters
---
Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

Setters
---
It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property # Getter
    def get_name(self):
        return self.name

    @get_name.setter # Setter
    def get_name(self, name):
        self.name = name


a = Person("Omprakash")
print(a.get_name) # Getter
a.get_name = "Paras"
print(a.get_name) # Setter