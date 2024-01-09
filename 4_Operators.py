"""
Operators
---

1. Arithmetic Operators
2. Logical Operators
3. Assignment Operators
4. Identity Operators
5. Comparison Operators
6. Membership Operators
7. Bitwise Operators
"""


# 1. Arithmetic Operators
print("5 + 5 is", 5+5)   # Addition
print("5 - 5 is", 5-5)   # Subtraction
print("5 * 5 is", 5*5)   # Multiplication
print("5 ** 5 is", 5**5) # Exponetial
print("5 / 5 is", 5/5)   # Division
print("5 // 5 is", 5//5) # Float
print("5 % 5 is", 5%5)   # Modulus


# 2. Logical Operators
# and Operator
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)
# or Operator
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)


# 3. Assignment Operators
a = 5
a += 5
print("a += 5 is", a)
a -= 5
print("a -= 5 is", a)
a *= 5
print("a *= 5 is", a)
a /= 5
print("a /= 5 is", a)
a %= 5
print("a %= 5 is", a)


# 4. Identity Operators
print("4 is 5 =", 4 is 5)
print("4 is not 5 =", 4 is not 5)


# 5. Comparison Operators or conditional operators
i = 2
print("i < 4 is", i<4)
print("i > 4 is", i>4)
print("i <= 4 is", i<=4)
print("i >= 4 is", i>=4)
print("i != 4 is", i!=4)
print("i == 4 is", i==4)


# 6. Membership Operators
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("2 in items =", 2 in items)
print("12 in items =", 12 in items)
print("4 not in items =", 4 not in items)
print("13 not in items =", 13 not in items)


# 7. Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print("0 & 1 is", 0 & 1)
print("0 | 1 is", 0 | 1)
print("1 & 2 is", 1 & 2)
print("1 | 2 is", 1 | 2)