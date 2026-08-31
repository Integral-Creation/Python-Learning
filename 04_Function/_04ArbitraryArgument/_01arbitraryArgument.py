"""
    Arbitrary Argument
        *args - allows us to pass multiple non-key argument
        **kwargs - allows us to pass multiple keyword argument
            * unpacking operator
"""

""" 1. *args"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5)) # 15

def display_name(*args):
    for arg in args:
        print(arg, end= " ")

display_name("Mr.", "Nikola", "Tesla") # Mr. Nikola Tesla 

""" 2. **kwargs"""
def print_address(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

print_address(
            street="8 west 40th st", 
            apt= "12",
            city="New York", 
            state="NY",
            pinCode=10018
        )

"""
output:
    8 west 40th st
    apt: 12
    city: New York
    state: NY
    pinCode: 10018
"""