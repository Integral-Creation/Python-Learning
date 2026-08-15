"""
Python has built in math module for following maths operations
| Function            | Purpose                 |
| ------------------- | ----------------------- |
| `math.pi`           | π = 3.141592653589793   |
| `math.e`            | e = 2.718281828459045   |
| `math.sqrt(x)`      | Square root             |
| `math.pow(x, y)`    | Power                   |
| `math.ceil(x)`      | Round up                |
| `math.floor(x)`     | Round down              |
| `math.fabs(x)`      | Absolute value          |
| `math.factorial(x)` | Factorial               |
| `math.gcd(a, b)`    | Greatest common divisor |
| `math.sin(x)`       | Sine                    |
| `math.cos(x)`       | Cosine                  |
| `math.tan(x)`       | Tangent                 |
"""
import math

# math.pi
print(math.pi) # 3.141592653589793

# math.e
print(math.e) # 2.718281828459045

# math.sqrt() -> Square root
print(math.sqrt(25)) # 5

# math.pow() -> Power
print(math.pow(2,3)) # 8.0

# math.ceil() -> Round up
print(math.ceil(4.2)) # 5

# math.floor() -> Round down
print(math.floor(4.8)) # 4

# math.fabs() -> Absolute Value
print(math.fabs(-5)) # 5.0

# math.factorial() -> Factorial 
print(math.factorial(5)) # 120

# math.gcd() -> Greatest Common Divisor
print(math.gcd(12,8)) # 4

# math.sin() -> Sine 
print(math.sin(math.pi / 2)) # 1.0

# math.cos() -> Cosine
print(math.cos(math.radians(0))) # 1.0

# math.tan() -> Tangent
print(math.tan(math.pi / 4)) # 0.9999999999999999