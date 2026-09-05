"""
    Recursion
        A function calling itself to solve the smaller parts of the same problem.

        Every Recursion functions has two key parts:
            • Base Case (Stopping conditions):
                Define when to stop the recursion
            • Recursive Case:
                the part where function call itself with smaller or simpler version of the same problem.
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120