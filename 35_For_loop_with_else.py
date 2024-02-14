# Else with for loop
for i in range(6):
    print("This is:", i)
    # If the loop is breaked then else block is not executed
    if i == 5:
        break
# Else block is executed when the loop end's
else:
    print("There are no values")


# Else with while loop
a = 0
while a < 5:
    print("This is:", a)
    a += 1
    if a == 2:
        break
else:
    print("While else is executed")