"""
    Dictionaries
     A collection of key:value pairs 
     ordered and changeable. No Duplicates

"""

""" 1. Creating Dict"""
    # 1. empty dictionaries
my_dict = dict()

students = {"01-2030-1010" : 'Nikola Tesla', "01-2030-1011" : "Einstein"}
print(students) # {'01-2030-1010': 'Nikola Tesla', '01-2030-1011': 'Einstein'}

""" 2. Modifying Dictionaries"""
    # 1. Adding
students["01-2030-1012"] = "Harry"
print(students) # {'01-2030-1010': 'Nikola Tesla', '01-2030-1011': 'Einstein', '01-2030-1012': 'Harry'}

    # 2. deleting
del students['01-2030-1012']
print(students) # {'01-2030-1010': 'Nikola Tesla', '01-2030-1011': 'Einstein'}

    # retrieving
print("Name: ", students["01-2030-1010"]) # Name:  Nikola Tesla

""" 3. Iterating Through Dictionaries"""
for key in students:
    print(f"Roll_no: {key} | Name: {students[key]}")
        # Roll_no: 01-2030-1010 | Name: Nikola Tesla
        # Roll_no: 01-2030-1011 | Name: Einstein

""" 4. Membership"""
print("01-2030-1011" in students) # True
print("01-2030-1013" in students) # False

""" 5. Equality"""
d1 = {1: 'a', 2 : 'b'}
d2 = {2 : 'b', 1 : 'a'}
  
print(d1 == d2) # True

""" 6. Dictionary Method"""
    # 1. keys() -> returns a sequence of keys
print(students.keys()) # dict_keys(['01-2030-1010', '01-2030-1011'])

    # 2. values() -> returns a sequence of values
print(students.values()) # dict_values(['Nikola Tesla', 'Einstein'])

    # 3. items() -> returns a tuple with key and values
print(students.items()) # dict_items([('01-2030-1010', 'Nikola Tesla'), ('01-2030-1011', 'Einstein')])

    # 4. get(key) -> return values for the key
print(students.get('01-2030-1010')) # Nikola Tesla

    # 5. pop(key) -> remove the values for the key
print(students.pop('01-2030-1011')) # Einstein
print(students) # {'01-2030-1010': 'Nikola Tesla'}

    # 6. popitem() -> returns a randomly selected key : values pairs as a tuple and removes the selected items
print(students.popitem())

    # 7. clear() -> delete the dictionary
students.clear()
print(students) 
# {}