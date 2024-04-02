# map() function
l = [i for i in range(1, 64)]
print(list(map(lambda x: x*x, l)))


# filter() function
# Function passed in filter() must return a boolean value
print(list(filter(lambda x: x%9==0, l)))


# reduce() function
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:
from functools import reduce
def multiply(x, y):
    return x*y

print(reduce(multiply, l))