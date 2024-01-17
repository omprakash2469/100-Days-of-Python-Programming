import time

# print(time.strftime("%H:%M:%S"))
# hour = int(time.strftime("%H"))
hour = int(input("Enter current time in (hour): "))

if hour >= 0 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17:
    print("Good Night")
else:
    print("Welcome to dreams")