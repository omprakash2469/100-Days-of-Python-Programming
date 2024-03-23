# File Input and Output ( IO )

"""
There are 6 access modes in Python:

Read Only ('r')
Read and Write ('r+')
Write Only ('w')
Write and Read ('w+')
Append Only ('a')
Append and Read ('a+')
"""

# File operation 
f = open("data/students.txt", "a+")
f.write("Hello world \nHow are you?")
text = f.read()
print(text)
f.close()

# File operation with keyword
with open("data/students.txt") as file:
    print(file.read())