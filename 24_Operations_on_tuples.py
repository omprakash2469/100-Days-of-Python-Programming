fruits = ("Apple", "Apple", "Banana", "Grapes", "Cherry")
choclates = ("Choclate", "Ice cream", "Dairy Milk", "Five Star")

# print(fruits.index("Apple")) # Finds the index of the given value 
# print(fruits.count("Apple")) # Returns the number of occurence of the given value

"""
 Add new item in tuple
"""
# You cannot add, update or delete items in tuple. You have to convert it to list and perform operations and convert back again to tuple
new_choclates = list(choclates) # convert to list
new_choclates.pop(2) # Remove element
new_choclates[2] = "Kinder Joy" # Update value of the element on the index `2`
choclates = tuple(new_choclates) # convert back to tuple

# Append two tuples
combined = fruits + choclates
print(combined)