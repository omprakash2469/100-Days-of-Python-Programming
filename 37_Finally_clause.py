# Finally clause in Exception Handling

num = input("Enter a number: ")

try: # code where error may occur
    num = int(num)
    print(f"Multiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

except ValueError: # handle error if occured
    print("Invalid input! Please enter an integer")
    
else: # code block if no error has occured
    print("Program is executed successfully!", num)
    
finally: # Whether the error has occured or not this block will be executed in both of the cases
    print("The task has ended")