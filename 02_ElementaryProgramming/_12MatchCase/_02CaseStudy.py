def isWeekend(day):
    match day:
            case 'Sunday' | 'saturday':
                return True
            case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
                return False
            case _:
                return False

print(isWeekend('Friday')) # False