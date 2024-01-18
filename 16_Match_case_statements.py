# Match Case Statements
"""
Match case statements only executes only one match and stop's if the case is matched
"""

x = int(input("Enter the value of x: "))

match x:
    case 10:
        print("This is the 10th case")
    case 20:
        print("This is the 20th case")
    case 30:
        print("This is the 30th case")
    case _ if x==40:
        print("This is the 40th case")
    case _ if x==50:
        print("This is the 50th case")
    case _:
        print("This is the default case")