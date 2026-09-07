"""
    Filter()
    it is used to select items from an iterable based on a conditions

    syntax:
        filter(function, iterable)
"""

num = [1,2,3,4,5,6,7,8]

def is_even(n):
    return n % 2 == 0

result = filter(is_even, num)
print(list(result)) # [2, 4, 6, 8]