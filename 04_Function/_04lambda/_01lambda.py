"""
    lambda function
    It is a small anonymous function, written in one line

    syntax:
        lambda `argument` : `expression`
"""

""" 1. Simple functions"""
def square(x):
    return x * x

print(square(5)) # 25

""" 2. using lambda functions"""
square_lambda = lambda x : x * x

print(square_lambda(5)) # 25

""" 3. multiple argument"""
add = lambda a, b : a + b

print(add(4,5)) # 9

""" 4. Use cases"""
    # 1. if - else
check = lambda x : "Positive" if x > 0 else "Negative"
print(check(-1)) # Negative

    # 2. List comprehension
func = [lambda arg= x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i(), end=" ")

    # 3. Return multiple result
add_mul = lambda a, b : (a + b, a * b)
print(add_mul(2, 4))