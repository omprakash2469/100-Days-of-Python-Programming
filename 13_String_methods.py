string = "This is my string"

# 1. Len
# Returns the length of the string
print(len(string))

# 2. String Cases
print(string.upper()) # - Makes a string in uppercase
print(string.lower()) # - Makes a string in lowercase
print(string.capitalize()) # - Makes first letter of a string uppercase
print(string.title()) # - Makes first letter of every string in uppercase

# 3. Rstrip
print(string.rstrip('-')) # - Removes any trailing characters

# 4. Split
print("bg-transparent.jpg".split(".")[-1]) # - Splits a string and returns an array

# 5. Center
# Aligns the string to the center as per the parameters given by the user
print(string.center(40))

# 6. Count
# Returns the number of times the given value has occured within the given string
print(string.count("s"))

# 7. Endswith
# Checks if the string ends with a given value and returns true or false
print(string.endswith("---"))
# We can also check for a value in-between the string by providing start and end index positions
print(string.endswith('s', 0, 4))

# 8. Find and index
# Search for the first index of the string and return the position of the string
# Find returns -1 if the value is not found
# Find returns error if the value is not found
print(string.find("is"))
# print(string.index("tsgis"))

# 9. isalnum()
# NOTE: Spaces are also considered
# Returns true only if the entire string only consists of A-Z, a-z, 0-9. Returns false if any other character occured
print(string.isalnum())

# 10. isalpha()
# NOTE: Spaces are also considered
# Returns true only if the entire string only consists of A-Z, a-z. Returns false if any other character occured
print(string.isalpha())

# 11. islower()
# Returns true if the given string is in lower case else it returns false
print(string.islower())

# 12. isprintable()
# Returns true if all values within the given string is printable else return false
print(string.isprintable())

# 13. isspaces()
# Returns true only and only if the string contains only white spaces, else returns false if any character found
print(string.isspace())

# 14. Check String Cases
# Returns true if the given string is in uppercase else returns false
print(string.isupper())

# Returns true if the given string is lower case else returns false
print(string.islower())

# Returns true if the first letter of every string is capital else return false
print(string.istitle())

# 15. startswith()
# Checks if the string starts with a given value and returns true or false
print(string.startswith('This'))

# 16. Swapcase()
# Changes to uppercase if the string is in the lowercase and changes to lowercase if the string is in uppercase
print(string.swapcase())