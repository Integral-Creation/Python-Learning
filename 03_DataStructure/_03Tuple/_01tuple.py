"""
    tuple
        A tuple is a collection of values that is:
            • Ordered - items have a fixed
            • Immutable - Once created, its items cannot change
            • Allow duplicate - allows multiple same value
            • Indexed - items are indexed
"""


""" 1. Creating tuple"""
number = (1,2,3,4,5)
print(number) # (1, 2, 3, 4, 5)

""" 2. Accessing tuple items"""
fruits = ("apple", "banana", "orange")

print(fruits[0])
print(fruits[1])
print(fruits[2])

""" 3. Tuple is immutable"""
# fruits[0] = 10 # TypeError: 'tuple' object does not support item assignment

""" 4. Tuple with duplicate values"""
numbers = (1,2,2,3,4,4,5)
print(numbers) # (1, 2, 2, 3, 4, 4, 5)

""" 5. Tuple Method"""
    # count()
numbers = (1,2,3,4,5,1)
print(numbers.count(1)) # 2

    # index()
print(numbers.index(4)) # 3

""" 6. Tuple unpacking"""
person = ("Nikola", 25, "Physics")
name, age, subject = person

print(name) # Nikola
print(age) # 25
print(subject) # Physics

""" 7. Tuple iteration"""
for i in numbers:
    print(i, end= " ") # 1 2 3 4 5 1