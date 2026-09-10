"""
    Match Case
        Python doesn't provide a traditional switch case like java, c++. Instead Python provides match-case, introduced in Python 3.10 ver
"""

def day_of_week(day):
    match day:
        case 1:
            return 'It is Sunday'
        case 2:
            return 'It is Monday'
        case 3:
            return 'It is Tuesday'
        case 4:
            return 'It is Wednesday'
        case 5:
            return 'It is Thursday'
        case 6:
            return 'It is Friday'
        case 7:
            return 'It is saturday'
        case _:
            return 'Not a valid day'

print(day_of_week(1)) # It is Sunday