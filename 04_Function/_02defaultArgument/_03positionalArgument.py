def billCalculation(quantity, price):
    bill = quantity * price 
    print(f"The total price for {quantity} products is {bill}")


quantity = int(input())
price = int(input())


billCalculation(quantity, price)
"""
Output:
5 
50
The total price for 5 products is 250
"""