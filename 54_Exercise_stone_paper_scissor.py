from random import choice

options = {
    1: "Stone",
    2: "Paper",
    3: "Scissor",
}

print("""Please select any one:
---
1. Stone
2. Paper
3. Scissor
""")

player = int(input("Enter your choice(Enter number): "))
computer = choice(list(options.keys()))

try:
    print("\nYour choice: ", options[player])
    print("Computer's choice:", options[computer])
    print()

    if player == 1 and computer == 3 or \
        player == 2 and computer == 1 or \
        player == 3 and computer == 2:
        print("You Won")
    elif(player == 1 and computer == 2 or \
        player == 2 and computer == 3 or \
        player == 3 and computer == 1):
        print("You Lose")
    else:
        print("Match Draw")
except:
    print("\nInvalid Input! Please select a valid input")