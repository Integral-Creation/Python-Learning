"""
    List 
        List is a collection of multiple values stored in a single variable
    
    List are:
        • Ordered - items have positions/ indexes
        • Mutable - can change,add, remove items
        • Allows duplicates
        • can contains different data type
"""

""" # 1 Creating list """
fruits = ["apple", "banana", "mango"]

print(fruits)

""" # 2 list Indexing"""
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # mango

# Negative index
print(fruits[-1]) # mango
print(fruits[-2]) # banana

""" # 3 Changing an items"""
fruits[1] = "orange"
print(fruits) # ['apple', 'orange', 'mango']

""" # 4 List Method"""
# append()
fruits.append("pineapple")
print(fruits) # ['apple', 'orange', 'mango', 'pineapple']

# insert()
fruits.insert(3, "kiwi")
print(fruits) # ['apple', 'orange', 'mango', 'kiwi', 'pineapple']

# remove()
fruits.remove("kiwi")
print(fruits) # ['apple', 'orange', 'mango', 'pineapple']

# pop()
fruits.pop(3)
print(fruits) # ['apple', 'orange', 'mango']

""" # 5 List length"""
print(len(fruits)) # 3

""" # 6 List Iteration"""
for i in fruits:
    print(i, end= " ")
# apple orange mango

""" # 7 Slicing """
num = [1,2,3,4,5,6]
print(num[1:4])
# [2, 3, 4]