import math

a = float(input('Enter side A : '))
b = float(input('Enter side B : '))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C: {round(c)}") 

"""
Output:
    Enter side A : 3
    Enter side B : 4
    Side C: 5
"""