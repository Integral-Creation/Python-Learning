# Python Calculator

operator = input('Enter an Operator(+ - * /): ')
num1 = float(input('Enter the 1st number'))
num2 = float(input('Enter the 2st number'))

if operator == '+':
    result = num1 + num2
    print("result:", round(result))
elif operator == '-':
    result = num1 - num2
    print("result:", round(result))
elif operator == '*':
    result = num1 * num2
    print("result:", round(result))
elif operator == '/':
    result = num1 / num2
    print("result:", round(result))
else:
    print(f"{operator} is not valid")