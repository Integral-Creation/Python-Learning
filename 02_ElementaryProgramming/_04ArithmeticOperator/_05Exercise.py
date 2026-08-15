import math

radius = float(input('Enter the radius of a circle: '))

area = math.pi * math.pow(radius, 2)
print(f"Area of circle of radius: {round(area)} cm²") 

"""
Output:
    Enter the radius of a circle: 5
    Area of circle of radius: 79 cm²
"""