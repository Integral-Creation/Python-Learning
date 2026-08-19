"""
    Logical operator
        it is used to combine or modify conditions and returns a Boolean result

            or -> at least one condition must be True
            and -> both conditions must be True
            not -> inverts the conditions (not False, Not True)
"""

temp = 20
is_raining = False
is_sunny = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny: 
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm Outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny: 
    print("It is COLD outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm Outside")
    print("It is cloudy")