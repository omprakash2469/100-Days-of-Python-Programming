"""
Class Variables
---
Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.
"""

class Employee:
    company_variable = "Apple"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"The employee name is {self.name} and he is {self.age} years old")

    
e1 = Employee("Omprakash", 22)
print(e1.name) # Instance variable
print(e1.age)
e1.show_details()


"""
Instance Variables
---
Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.
"""
print(e1.company_variable) # Class variable