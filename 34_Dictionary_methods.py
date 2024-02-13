# Dictionary Methods
car = {
    "name": "Mercedes Benz",
    "color": "Black",
    "model": "GLE 500",
    "year": 2019,
}

# 1. update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
car.update({'model': 'GLE 400'}) # Update the existing key
car.update({'city': 'Jaipur'}) # Create a new key
# print(car)


# 2. clear()
# The clear() method removes all the items from the list.
# car.clear()
print(car)


# 3. pop()
# The pop() method removes the key-value pair whose key is passed as a parameter.
car.pop("city")
print(car)


# 4. popitem()
# The popitem() method removes the last key-value pair from the dictionary.
car.popitem()
print(car)


# 4. del
# we can also use the del keyword to remove a dictionary item.
# If key is not provided, then the del keyword will delete the dictionary entirely.
del car['model']
print(car)
