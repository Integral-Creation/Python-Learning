"""
    Nested Loop
        a loop within another loop
"""

for i in range(1, 6):
    for j in range(i):
        print("*", end= " ")
    print()

"""
Output:
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
"""