"""
    input()
        A function that prompts the user to enter data
        returns the entered data as string
"""

name = input("What is your name?: ")
age = int(input("How old are you?: "))

print(f"Hello {name}!")
print(f"You are {age} year old")

"""
Output:
    What is your name?: Nikola
    How old are you?: 25
    Hello Nikola!
    You are 25 year old
"""