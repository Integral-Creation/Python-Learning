"""
    Custom Exception using try and except
"""

class InvalidAgeError(Exception):
    pass
try:
    age = int(input('Enter your age: '))
    if age < 0:
        raise InvalidAgeError('Age cannot be negative')
    elif age == 0:
        raise InvalidAgeError('Age cannot be Zero')

    print('Your age is ', age)
except InvalidAgeError as e:
    print("Error: ", e)

"""
Output:
    Enter your age: -1
    Error:  Age cannot be negative

    Enter your age: 25
    Your age is  25
"""