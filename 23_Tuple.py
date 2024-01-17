"""
1. Tuples

Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are seperated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we cannot alter them after creation.
"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# It can contain multiple data types
mix_tuple = ("Hello", 1, True, None, [1, 2], {"hello": "world"}, 2.342)

# Tuple's index starts with 0
# It also has Positive and Negative indexing same as list
print(mix_tuple[4]) # Positive indexing
print(mix_tuple[-4]) # Negative indexing