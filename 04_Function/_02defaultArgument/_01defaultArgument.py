"""
    Default argument
    A default argument is a function parameter that already has a value. 
    If user doesn't Provide the value python uses the default value.
    It makes function more flexible.
"""

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05)) # 525.0

print(net_price(500)) # 525.0 # using default argument doesn't required all the argument