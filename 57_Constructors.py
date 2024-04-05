"""
A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
"""

class Person:
    # __init__ method runs on the initialization of an object.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Hello {name}")

    # bio of the person
    def bio(self):
        print(f"{self.name} is {self.age} year's old")


p1 = Person("Paras", 24)
p2 = Person("Omprakash", 26)
p1.bio()
p2.bio()