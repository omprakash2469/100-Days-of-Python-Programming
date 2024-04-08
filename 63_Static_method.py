"""
Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self).

They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.
"""

class Human:
    def __init__(self, values):
        self.values = values

    def get_values(self):
        return self.values
    
    @staticmethod
    def multiply(a, b):
        return a*b
    
a = Human(45)
print(a.values)
print(a.get_values())
print(a.multiply(101, 20))