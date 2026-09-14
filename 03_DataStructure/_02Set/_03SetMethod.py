set1 = {1,2,3}
set2 = {3,4,2}

""" 1. Union """
print(set1.union(set2)) # {1, 2, 3, 4, 5}
print(set1 | set2)      # {1, 2, 3, 4, 5}

""" 2. Intersection"""
print(set1.intersection(set2)) # {2, 3}
print(set1 & set2)             # {2, 3}

""" 3. Difference""" 
print(set1.difference(set2)) # {1}
print(set1 - set2)           # {1}

""" 4. Symmetric difference"""
print(set1.symmetric_difference(set2)) # {1, 4}