# Enuemrate Function
# Enumerate function provide the index of each iteration
# List
fruits = ['Apple', 'Mango', 'Grapes', 'Banana', 'Orange']

students = [
    {
        "name": "Omprakash",
        "location": "Rajasthan"
    },
    {
        "name": "Paras",
        "location": "Maharashtra"
    },
    {
        "name": "Kiran",
        "location": "Chennai"
    },
    {
        "name": "Niraj",
        "location": "Heaven"
    },
]



# Iterate over list
# --
# for i, value in enumerate(fruits):
#     print(value, "is at index", i)



# Iterate over object
# --
for i, value in enumerate(students):
    print(i)
    print(value['name'], "is from", value['location'])
