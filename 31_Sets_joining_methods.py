"""
Methods in sets

Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

1. union()
2. update()
3. intersection()
4. intersection_update()
5. symmetric_difference()
6. symmetric_difference_update()

"""

animes = {"Pokemon", "Doraemon", "Dragon Ball z", "Naruto"}
games = {"COC", "Prince of Persia", "War 3", "Pokemon Leaf Green", "Pokemon"}


"""
1. union()
Add two sets and returns a new set

It returns the new set and does not update the existing set
"""
# print(animes.union(games))


"""
2. update()
Add items into the existing set from the another set

It updates the existing set with the new set
"""

# animes.update(games)
# print(animes)


"""
3. intersection()
intersection() returns items that are similar to both sets

It returns the new set and does not update the existing set
"""
# print(animes.intersection(games))


"""
4. intersection_update()
intersection_update() returns items that are similar to both sets

It updates the existing set and returns None
"""
# animes.intersection_update(games)
# print(animes)


"""
5. symmetric_difference()
symmetric_difference() returns items that are not similar to both sets

It returns the new set and does not update the existing set
"""
# print(animes.symmetric_difference(games))


"""
6. symmetric_difference_update()
symmetric_difference_update() returns items that are not similar to both sets

It updates the existing set and returns None
"""
# animes.symmetric_difference_update(games)
# print(animes)


"""
7. difference()
difference() returns items that are only present in the original set and not in both the sets

It returns the new set and does not update the existing set
"""
# print(animes.difference(games))


"""
8. difference_update()
difference_update() returns items that are only present in the original set and not in both the sets

It updates the existing set and returns None
"""
animes.difference_update(games)
print(animes)
