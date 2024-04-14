"""
Magic/Dunder Methods in Python
---
These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

"""


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f"{self.id} - {self.name}")

    
    def __str__(self):
        return f"<Employee {self.name} str>"
    
    def __repr__(self):
        return f"<Employee {self.name} repr>"


a = Employee("Paras", 101)


"""
__str__ and __repr__ methods
---
The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

"""
print(str(a))
print(repr(a))