# Record the list of students in a file

name = input("Enter Your Name: ")

with open("data/students_list.txt", "a") as append:
    append.write(f"{name}\n")