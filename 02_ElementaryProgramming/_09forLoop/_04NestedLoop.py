r = int(input('Enter the # of rows: '))
c = int(input('Enter the # of column: '))

symbol = input('Enter a symbol to use: ')

for i in range(r):
    for j in range(c):
        print(symbol, end= " ")
    print()

"""
Output:
    Enter the # of rows: 5
    Enter the # of column: 5
    Enter a symbol to use: @
    @ @ @ @ @ 
    @ @ @ @ @ 
    @ @ @ @ @ 
    @ @ @ @ @ 
    @ @ @ @ @ 
"""