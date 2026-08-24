"""
    set
        A set is a collection of unique values
        values are unordered and immutable
"""

my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}

""" 1. Set Properties"""
    # 1 set don't allows duplicate
my_set = {1,2,2,4,3,4,3,7}
print(my_set) # {1, 2, 3, 4, 7}

    # 2 set are unordered
fruits = {"apple", "banana", "mango", "orange"}
print(fruits) # {'orange', 'apple', 'banana', 'mango'} # order of output should change

""" 2. Creating empty set"""
x = {}

new_set = set()

""" 3. Adding values"""
num = {1,2,3,4}
num.add(5)
print(num) # {1, 2, 3, 4, 5}

""" 4. Removing values"""
num.remove(3)
print(num) # {1, 2, 4, 5} 
    # remove gives error if values not found in set, thus use discard() method

""" 5. Membership operator""" 
num = {10,20,30}
print(10 in num) # True
print(40 in num) # False

""" 6. Set operations"""
a = {1,2,3}
b = {3,4,5,1}

    #  Union 
print(a | b) # {1, 2, 3, 4, 5}
    # intersection - values common to both
print(a & b) # {1, 3}
    # difference - values in `a` but *not in* `b`
print(a - b) # {2}
    # symmetric  difference - values not common in both
print(a ^ b) # {2, 4, 5}