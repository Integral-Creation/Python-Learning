"""
    Set relations:
        issuperset - 
        issubset - 
        isdisjoint
"""

# issubset()
a = {1,2,3,4,5}
b = {2,3,4}

print(a.issubset(b)) # False
print(b.issubset(a)) # True

# issuperset()
print(a.issuperset(b)) # True
print(b.issuperset(a)) # False

c = {6,7,8}

print(a.isdisjoint(b)) # False
print(a.isdisjoint(c)) # True