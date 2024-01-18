str = "Omprakash"

## Both are Equal
# Prints the characters from 0-2. It includes 0 but doesn't include 2
print(str[:2])
print(str[0:2])

## Printing a part of string
# Prints from 2 - (len of string)
print(str[2:])

## Print length of string
length = len(str)
print("The length of string is:", length)

# Syntax: slice(start, stop, step)
## Negative Slicing

"""
Same as
str[9-1:9-7]
str[8:2]
8 - 2 is not correct syntax, so it prints nothing
"""
# Both are same
# print(str[length-1:length-7])
# print(str[-1: -7])

# Same as: str[2:8]
print(str[-7: -1])