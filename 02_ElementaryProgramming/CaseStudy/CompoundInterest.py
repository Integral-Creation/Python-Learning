# Compound Interest 

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in year: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: {total:.2f}")


"""
Output:
    Enter the principle amount: 1000
    Enter the rate: 10
    Enter the time in year: 1
    Balance after 1.0 year/s: 1100.00
"""