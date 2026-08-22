"""
    While loop
        A while loop repeatedly execute a block of code as long as a conditions are True.

        syntax
            while condition:
                # code to execute
"""

name = input("Enter your name: ")

while name == "":
    print("you did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}!")

"""
Output:
    Enter your name: 
    you did not enter your name
    Enter your name: Tesla
    Hello Tesla!
"""