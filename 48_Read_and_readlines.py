# File write content
with open("data/students.txt", "r+") as file:
    # Writing in file
    friends = ["Omprakash", "Paras", "Niraj", "Kiran", "Omkar", "Manish"]
    for  friend in friends:
        file.write(f"Hello! {friend}, How are you?")

# Read file content
with open("data/students.txt") as file:
    print(file.read()) # Read text
    # print(file.readline()) # Read single line
    # print(file.readlines()) # Read all lines