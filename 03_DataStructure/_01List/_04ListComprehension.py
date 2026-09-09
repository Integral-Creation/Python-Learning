"""
    List comprehension:
        A concise and easier to read than traditional loops
        syntax:
            [expression for value in iterable if condition]
"""

doubles = []
""" Loop method"""
for x in range(1, 6):
    doubles.append(x * 2)

print(doubles) # [2, 4, 6, 8, 10]

""" using List comprehension"""
doubles = [x * 2 for x in range(1, 11)]
print(doubles) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.upper() for fruit in fruits]

print(fruits) # ['APPLE', 'ORANGE', 'BANANA', 'COCONUT']