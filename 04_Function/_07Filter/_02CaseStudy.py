"""
    Filter using lambda 
"""

num = [1,2,3,4,5,6,7,8]

result = filter(lambda x : x % 2 == 0, num)
print(list(result)) # [2, 4, 6, 8]
