"""
    for loop
        it execute a block of code a fixed number of times.
"""

for x in range(1,11):
    print(x, end= " ")
# Output: 1 2 3 4 5 6 7 8 9 10 

print()

for x in reversed(range(1,11)):
    print(x, end= " ")
# Output: 10 9 8 7 6 5 4 3 2 1 

print()

for x in range(1,11,2):
    print(x, end= " ")
# Output: 1 3 5 7 9

print()

for x in range(1,11):
    if x == 13:
        break
    print(x, end= " ")
# Output: 1 2 3 4 5 6 7 8 9 10 