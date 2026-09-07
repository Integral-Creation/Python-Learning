"""
    Iterables
        An Iterable is any object that can be looped through one item at a time.
"""

""" 1. List Iterable"""
number = [1,2,3,4,5]

for num in number:
    print(num, end=" ") # 1 2 3 4 5 

""" 2. Set Iterable"""
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit, end=" ") # apple coconut orange banana

""" 3. String Iterable"""
name = "Tesla"

for char in name:
    print(char, end="-") # T-e-s-l-a-

print()

""" 4. Dictionary Iterable"""
my_dict = {"A":1, "B":2, "C":3, "D":4}

for key in my_dict:
    print(key, end=" ") # A B C D 

for val in my_dict.values():
    print(val, end=" ") # 1 2 3 4

print()

for key, val in my_dict.items():
    print(key, val)

"""
Output:
    A 1
    B 2
    C 3
    D 4
"""