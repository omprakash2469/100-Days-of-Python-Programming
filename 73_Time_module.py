import time

current_time = time.localtime()

# DateTime format representation
time_format = "%d %b, %Y %H:%M:%S"
print(time.strftime(time_format, current_time))

for i in range(11):
    print(i * "*")
    time.sleep(1) # Pause the code for the given time period