"""
    Indexing 
        accessing elements of a sequence using [] (indexing operator)
        [start : end : step]
            starting index is inclusive
            ending index is exclusive

"""

num = "123-45-6-78"
print(num[4])
# Output: 4

print(num[0:5])
# Output: 123-4

print(num[5:9])
# Output: 5-6-

print(num[5:])
# Output: 5-6-78

print(num[-1])
# Output: 8

print(num[::2])
# Output: 134--8

print(num[::-1])
# Output: 87-6-54-321