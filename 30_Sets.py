"""
Sets

Set is a collection of well defined objects.

Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackers {}. Sets are unchangeable, meaning you cannot change items of the sets once created. Sets do not contain duplicate items.

Items in the sets cannot be access with index numbers

You cannot update the items of the sets once created. You can only add or remove items

If the set is empty then it's type is 'dict' not 'set'. Once you have items in it then it becomes a 'set'.
"""

animes = {"Pokemon", "Doraemon", "Naruto", "Dragon Ball Z"}
print(animes)

# Access set items
for anime in animes:
    print(anime)