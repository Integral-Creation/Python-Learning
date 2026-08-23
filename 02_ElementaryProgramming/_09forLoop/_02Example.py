import time
my_time = int(input('Enter the time in second: '))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up")

"""
Output:
    Enter the time in second: 5
    00:00:05
    00:00:04
    00:00:03
    00:00:02
    00:00:01
    Time is up
"""