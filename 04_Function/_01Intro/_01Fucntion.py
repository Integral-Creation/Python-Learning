"""
    Function
    A function is a reusable block of code that perform specific task.
    Instead of writing the same code repeatedly, write it once and call it whenever you need it

    syntax:
        def function_name(parameter):
            # code
"""

""" 1. Basic Function"""
def greet():
    print("Hello")

greet()

""" 2. function with parameter"""
def greet(name):
    print(f"Hello {name}")

greet("Tesla") # Hello Tesla

""" 3. function with multiple parameter"""
def add(a, b):
    print(a + b)

add(2, 4) # 6

""" 4. return statement"""
def add(a, b):
    return a + b

print(add(10,2)) # 12