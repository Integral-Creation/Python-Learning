"""
    Typecasting 
        It is a process of converting a variable from a one data to another
        str(), int(), float(), bool()
"""

name = "Tesla"
age = 25
gpa = 9.8
is_Student =True

gpa = int(gpa)
print(gpa) # Output: 9

age = float(age)
print(age) # Output: 25.0

age = str(age)
print(type(age)) # Output: <class 'str'>

name = bool(name)
print(name) # Output: True