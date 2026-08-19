"""
    Conditional Expression
        A one line shortcut for if-else statement(Ternary operator)
"""
num = 5

result = "EVEN" if num % 2 == 0 else "ODD"
print(f"{num} is:",result, end= " ")
print("Positive" if num > 0 else "Negative")

a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b
print(f"max num ({a}, {b}):",max_num)
print(f"min num ({a}, {b}):",min_num)
