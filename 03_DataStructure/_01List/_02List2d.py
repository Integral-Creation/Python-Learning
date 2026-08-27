"""
    2D list:
        2-Dimensional list in Python is basically a list containing another list 
"""
""" 1. Creating a 2D list"""
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(numbers) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

""" 2. Accessing Element"""
print(numbers[1][2]) # Output: 6

""" 3. Changing values"""
numbers[0][0] = 0
print(numbers) # [[0, 2, 3], [4, 5, 6], [7, 8, 9]

""" 4. For loop"""
for row in numbers:
    for value in row:
        print(value, end= " ")
    print()
"""
    0 2 3 
    4 5 6 
    7 8 9 
"""