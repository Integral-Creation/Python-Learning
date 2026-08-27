fruits = ["apple", "orange", "banana", "coconut"]
vegetable = ["carrots", "potato", "lettuce"]

groceries = [fruits, vegetable]

print(groceries) # Output: [['apple', 'orange', 'banana', 'coconut'], ['carrots', 'potato', 'lettuce']]

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()
"""
    apple orange banana coconut 
    carrots potato lettuce  
"""