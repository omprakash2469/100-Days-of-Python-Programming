"""
Dictionary

Dictionary are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
"""

student = {
    "name": "Vishnu Singh",
    "roll_no": 54,
    "class": "11th",
    "field": "Commerce",
    "age": 24
}

# Returns value of a given key. If the key is not found in dictionary it returns None.
print(student.get('address')) 

# Returns value of a given key. If the key is not found in dictionary it throws `KeyError`.
print(student['name']) 

# Returns a list of all keys
print(student.keys()) 

# Returns a list of all values
print(student.values()) 

# Returns a list of all values
print(student.items())
