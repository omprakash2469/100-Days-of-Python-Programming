sets = [
    # Question -- Options -- Correct Answer
    ["Which is not a programming language?", ["Python", "Javascript", "HTML", "PHP"], "HTML"],
    ["Which is a Backend Framework?", ["Ruby", "Django", "Python", "React"], "Django"],
    ["Which is Javascript Framework", ["Pandas", "NumPy", "React Js", "Node.Js"], "React Js"],
    ["Which is an Alien?", ["Developer", "Designer", "Marketer", "Analyst"], "Developer"],
]

i = 0
score = 0
while (i < len(sets)):
    # Print question
    print("============")
    print(sets[i][0])
    print("============")

    # Print answer
    for j in range(1, len(sets[i][1]) + 1):
        print(f"Option {j} - {sets[i][1][j - 1]}")

    # Answer prompt
    answer = int(input("Select correct option: "))

    print()

    # Get correct answer
    index_of_answer = sets[i][1].index(sets[i][2])

    # Check correct answer
    if answer - 1 == index_of_answer:
        score += 500
        

    # Go to next question
    i += 1

print("Your score is:", score)
print(f"Your {int(score/500)} answers are correct")