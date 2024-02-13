# Sets Methods

integers = {"one", "two", "three", "four"}
numbers = {"five", "six", "seven", "eight", "ten"}
nums = {"five", "six", "seven"}

# 1. isdisjoint()
# It checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
# print(integers.isdisjoint(numbers))


# 2. issuperset()
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
# print(integers.issuperset(numbers))


# 3. issubset()
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
# print(nums.issubset(numbers))


# 4. add()
# If you want to add a single item to the set use the add() method.
# nums.add("nine")
# print(nums)


# 5. update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
# nums.add("nine")


# 6. remove() / discard()
# We can use remove() and discard() methods to remove items form list.
# numbers.remove("sixd") # Throws error if the 'key' is not present in the set
# numbers.discard("sixd") # Doesn't throws error if the 'key' is not present in the set
# print(numbers)


# 7. pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
# Every time different value pops out when we call pop().

# popped_value = numbers.pop()
# print(popped_value)


# 8. del
# del is not a method, rather it is a keyword which deletes the set entirely.
# del numbers


# 8. clear()
# This method clears all items in the set and prints an empty set.
# numbers.clear()
# print(numbers)


# 9. Validate if item exists in set
if 'six' in numbers:
    print("Yes it exists")
else:
    print("Item not found")