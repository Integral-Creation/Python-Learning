"""
    Custom Exception 
        Custom Exception allows you to define application-specific errors that are not covered by python Built in exception.

    syntax:
        class CustomExceptionName(Exception):
            pass
"""

""" 1. Creating a Custom Exception"""
class InvalidAgeError(Exception):
    pass

age = int(input('Enter your age: '))

if age < 0:
    raise InvalidAgeError('Age cannot be negative')
elif age == 0:
    raise InvalidAgeError('Age cannot be Zero')

print('Your age is ', age)
"""
output:
Enter your age: 0
    InvalidAgeError: Age cannot be Zero

Enter your age: -9
    InvalidAgeError: Age cannot be negative
"""