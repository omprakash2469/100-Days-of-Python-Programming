"""
The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.
"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f"{self.id} - {self.name}")
    

class Programmer(Employee):
    def __init__(self, name, id, language):
        self.language = language
        super().__init__(name, id) # use super keyword to all parent class's methods


a1 = Employee("Omprakash", 2469)
a2 = Programmer("Paras Shewale", 1340, "Python")
a1.info()
a2.info()