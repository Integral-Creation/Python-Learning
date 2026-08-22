"""
    Format specifiers
        {:flags} format a value based on what flags are inserted
    
    .(number)f = round to that many decimal place (Fixed points)
    :(number)  = allocate that many spaces
    :03  = allocate and zero pad that many spaces
    :<   = left justify
    :>   = right justify
    :^   = center align
    :+   = use a plus sign to indicate positive value
    :=   = place sign to the leftmost position
    :    = insert a space before positive number
    :,   = comma separator
"""

price1 = 3.14159
price2 = -343.343
price3 = 12.345

print(f"price 1 is {price1:.2f}")
# Output: price 1 is 3.14
print(f"price 2 is {price2:25}")
# Output: price 2 is                  -343.343
print(f"price 3 is {price3:010}")
# Output: price 3 is 000012.345


print(f"price 1 is ${price1:<10}")
# Output: price 1 is $3.14159  
print(f"price 2 is ${price2:>10}")
# Output: price 2 is $  -343.343
print(f"price 3 is ${price3:^10}")
# Output: price 3 is $  12.345


print(f"price 1 is ${price1:+}")
# Output: price 1 is $+3.14159  
print(f"price 2 is ${price2:-}")
# Output: price 2 is $-343.343
print(f"price 3 is ${price3: }")
# Output: price 3 is $ 12.345


price1 = 3456.080
print(f"price 1 is ${price1:,}")
# Output: price 1 is $3,456.08  