# Seek(), tell(), truncate() function

"""
seek() function
---
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:

"""

with open("data/students_list.txt", "r") as file:
    # Read the first line and count the characters
    length = len(file.readline())

    # Skip the x number of characters from the file
    # file.seek(10)
    file.seek(length + 1)

    # Read the file
    print(file.read())


"""
tell() function
---
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:

"""

with open("data/students_list.txt", "r") as file:
    file.seek(10) # set current position to 10

    print(file.tell()) # Get the current position
    print(file.read()) # Read the file


"""
truncate() function
---
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

Here is an example of how to use the truncate function:

"""

with open("data/demo.txt", "w") as file:
    file.write("Omprakash Prajapati")
    file.truncate(5)
    # file.truncate(4) # set current position to 10

with open("data/demo.txt", "r") as file:
    print(file.read())