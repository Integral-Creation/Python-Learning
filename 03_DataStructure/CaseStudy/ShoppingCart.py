# Shopping cart Program

foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("------Your Cart-----")
for i in range(len(foods)):
    print(f"{foods[i]} -> {prices[i]}")
    total += prices[i]

print(f"Total: {total}")

"""
Output:
        Enter a food to buy (q to quit): idli and dosa 
        Enter the price of a idli and dosa: 500
        Enter a food to buy (q to quit): flattened rice (poha)
        Enter the price of a flattened rice (poha): 40
        Enter a food to buy (q to quit): Paratha
        Enter the price of a Paratha: 50
        Enter a food to buy (q to quit): q
        ------Your Cart-----
        idli and dosa -> 500.0
        flattened rice (poha) -> 40.0
        Paratha -> 50.0
        Total: 590.0
"""