item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: Rs {total}")

"""
Output:
    What item would you like to buy?: MilkShake
    What is the price?: 200
    How many would you like?: 4
    You have bought 4 x MilkShake/s
    Your total is: Rs 800.0 
"""