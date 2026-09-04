# user input
price = float(input("Enter price: "))

# discount input
discount_percentage = float(input('Enter discount: '))

# lambda function
apply_discount = lambda price, discount_percentage: price - (price * (discount_percentage / 100))

print(f"Final amount: {apply_discount(price, discount_percentage)}")

"""
Output:
        Enter price: 150
        Enter discount: 75
        Final amount: 37.5
"""