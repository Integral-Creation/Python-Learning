"""
Mathematical Operations

abs()       → absolute value
round()     → round a number
max()       → largest
min()       → smallest
sum()       → total
pow()       → power
divmod()    → quotient + remainder
"""
w = 4
x = 10
y = -10
z = 4.14

# abs()
print(abs(x)) # output: 10
print(abs(y)) # output: 10

# round()
print(round(z)) # output: 4

# max()
print(max(x,y,z)) # output: 10

# min()
print(min(x,y,z)) # output: -10

# sum()
num = [1,2,3,4,5]
print(sum(num)) # output: 15

# pow()
print(pow(2,3)) # output: 8

# divmod()
print(divmod(10,3)) # output: (3, 1)
print(10 // 3) # quotient -> 3
print(10 % 3) # remainder -> 1
