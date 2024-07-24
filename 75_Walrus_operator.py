# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

## Example 1
# first = True
# print(first:=False) # Assigns value within an expression.

## Example 2
# numbers = [i for i in range(10)]

# while (n:=len(numbers) > 0):
#     print(numbers.pop())

## Example 3
names = list()
while (name:=input("Enter Your Name: ") != "quit"):
    names.append(name)

print(names)
