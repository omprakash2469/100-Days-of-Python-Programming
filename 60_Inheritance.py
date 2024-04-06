"""
Inheritance
---
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
"""

class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def info(self):
        print(f"{self.name} is {self.age} and lives in {self.location}")


a = Person("Omprakash", 21, "Pune")
a.info() # Run the method


# Create a new class by inheriting the above class
class Programmer(Person):
    def lang(self):
        print(f"Python is the favorite language of {self.name}.")

b = Programmer("Omii", 22, "Delhi")
b.info()
b.lang()


"""
Types of inheritance:
---
Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance
"""

