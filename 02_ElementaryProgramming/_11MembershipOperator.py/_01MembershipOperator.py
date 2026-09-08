"""
    Membership Operator
        Membership operator in Python check weather a value exits in a sequence or collection
            •  `in` : returns true if value exists
            •  `not in` : returns false if value does not exists
"""

""" `in` operator`"""
number = [1,2,3,4,5]
print(3 in number) # True

""" `not in` operator`"""
print(4 not in number) # False

""" with String"""
word = 'Python'
print('t' in word) # True

""" with sets"""
students = {'tesla','einstein','newton'}
print('tesla' in students) # True

""" with tuple"""
colors = ("red", "green", "blue")

print('blue' in colors) # True

""" with dictionary"""
grade = {"Anby":'A', "Jane": 'A+', "Veli": 'O'}
student = 'Jane'

if student in grade:
    print(f"{student}'s grade is {grade[student]}")
else:
    print(f"{student} was not found")
# Jane's grade is A+