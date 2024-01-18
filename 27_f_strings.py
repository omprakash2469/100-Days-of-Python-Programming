"""
String formatting

String formatting can be done in python using the format method.
"""
txt = "For only {price} dollars!"
# print(txt.format(price = 49))


"""
f strings

It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

"""

name = "Omprakash Prajapati"
profession = "Software Engineer"
location = "Jodhpur, Rajasthan"

print(f"Hello! My name is {name} and I am a {profession} based in {location}")