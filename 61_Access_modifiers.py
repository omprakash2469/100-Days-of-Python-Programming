"""
Access Specifiers/Modifiers
=========================
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:

Types of access specifiers
------
Public access modifier
Private access modifier
Protected access modifier
"""

class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable
        self.__location = "Pune"     # private variable

    def _info(self):  # An indication of protected function
        return f"{self.name} is {self.age} years old"

    def __funName(self):  # An indication of private function
        self.number = 34
        return self.number

obj = Student(21,"Omprakash")


# 1. Public Access modifier
# -----------
# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

print(obj.age)
print(obj.name)



# 2. Private Access Modifier
# -----------
# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

# Name mangling
# ---
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

# print(obj.__location) # Cannot be accessed directly
# print(obj.__funName()) # Cannot be accessed directly
print(obj._Student__location) # Can be accessed indirectly
print(obj._Student__funName()) # Can be accessed indirectly



# 3. Protected Access Modifier
# -----------

# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

print(obj._info()) # intended to access from within the class
