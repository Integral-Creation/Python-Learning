food = input("Enter a food you likes (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you likes (q to quit): ")

print("Thank you")

"""
Output:
    Enter a food you likes (q to quit): MilkShake 
    You like MilkShake
    Enter a food you likes (q to quit): q
    Thank you
"""