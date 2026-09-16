num_items = int(input('Enter number of item: '))
inventory = {}

for i in range(num_items):
    item_name = input('Enter Item name: ')
    item_quantity = int(input('Enter Item Quantity: '))
    inventory[item_name] = item_quantity

print('Inventory : ', inventory)
search = input('Enter Item to search: ')

if search in inventory:
    removed_quantity = inventory.pop(search)
else:
    removed_quantity = "key not found"

print(f"Item {search} : {removed_quantity}")
print("Update inventory: ")
print(inventory)

"""
Output:
        Enter number of item: 3
        Enter Item name: Sword
        Enter Item Quantity: 2
        Enter Item name: Shield
        Enter Item Quantity: 2
        Enter Item name: Potion
        Enter Item Quantity: 10
        Inventory :  {'Sword': 2, 'Shield': 2, 'Potion': 10}
        Enter Item to search: Shield
        Item Shield : 2
        Update inventory: 
        {'Sword': 2, 'Potion': 10}
"""