"""
1. Lists
---
    - Lists are ordered collection of data items.
    - They store multiple items in a single variable.
    - List items are separated by commas and enclosed within square brackets [].
    - Lists are changeable meaning we can alter them after creation.
"""
fruit = ["Mango", "Apple", "Grapes", "Banana"]
pokemon = ["Pikachu", "Charizard", "Greninja", "Infernape"]

# print("These are fruits: ", fruit)
# print("These are pokemons: ", pokemon)



"""
2. List Index
---

Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on
"""

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]   - Positive Indexing
#     [0] or [-5]   [-4]    [-3]     [-2]     [-1]   - Negative Indexing


# Positive Indexing
# Count starts from 0
# print(colors[2]) # Output: "Blue"

# Negative Indexing
# Count starts from -1
# print(colors[-2]) # Output: "Yellow"


"""
3. Check whether an item in present in the list?
"""
if("Blue" in colors):
    print("Blue is Present")
else:
    print("Blue is not Present")



"""
4. Range in index
---

You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

"""

# Syntax
# listName[start : end : jumpIndex]
games = ["GTA", "COD", "COC", "PUBG", "BGMI", "Free Fire"]
print(games[::2])
# Jumps to every 2nd element
# Output:
#   - ['GTA', 'COC', 'BGMI']

# Count list elements
print(len(games))