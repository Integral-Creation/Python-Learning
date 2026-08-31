"""
    Exception handling
        It allows the program to handle unexpected errors during executions in a controlled way, instead of crashing abruptly.

    syntax:
        try:
            # error causing code
        except SomeException:
            # code
        else:
            # code
        finally:
            # code
"""

""" 1. try except block"""
n = 10
try:
    n / 0
except:
    print("can't divide by zero!")


""" 2. catching specific exception"""
try:
    num = int(input('Enter a Number: '))
except ValueError:
    print("Please Enter a valid input!")
        # Enter a Number: zero
        # Please Enter a valid input!


""" 3. else block"""
try:
    num = int(input('Enter a number: '))
except ValueError:
    print('Invalid input')
else:
    print('You entered: ', num)
        # Enter a number: 1
        # You entered:  1


""" 4. finally block"""
try:
    num = int(input('Enter a number: '))
except ValueError:
    print('Not a Number')
finally:
    print('finis')
        # Enter a number: 3
        # finis