import time

# Get the current hour
hour = time.strftime("%H")

if hour<"12":
    print("Good Morning")
elif(hour>"12" and hour<"20"):
    print("Good Evening")
else:
    print("Good Night")