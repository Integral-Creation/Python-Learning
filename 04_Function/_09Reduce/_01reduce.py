"""
The reduce() function in Python repeatedly applies a function to the elements of an iterable (like a list or tuple) from left to right, combining them step-by-step to reduce the entire sequence down to a single value
"""

from functools import reduce

num = [1,2,3,4,5]

result = reduce(lambda x, y: x + y, num)
print(result)