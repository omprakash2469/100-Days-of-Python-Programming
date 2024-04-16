"""
Method Overriding in Python
---
Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.
"""

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Shape is initialized")
    
    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius



# rec = Shape(5, 10)
circle = Circle(45)
print(circle.area())