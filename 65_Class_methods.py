"""
What are Python Class Methods?
---
A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

"""

"""
Why Use Python Class Methods?
---
Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.
"""


class Employee:
    company_variable = "Apple"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod # to change the value of a variable on a class level
    def change_company(self):
        self.company_variable = "Tesla"
    
    def show_details(self):
        print(f"The employee name is {self.name} and he is {self.age} years old")


# Creating an object of the class
a1 = Employee("Omprakash", 20)
a1.show_details()
print(Employee.company_variable) # class variable
a1.change_company()
# print(a1.company_variable) # Instance variable
print(Employee.company_variable) # class variable