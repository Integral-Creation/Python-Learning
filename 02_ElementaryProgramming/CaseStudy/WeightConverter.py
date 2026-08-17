weight = float(input('Enter your weight: '))
unit = input('Kilogram or Pounds? (K/L): ')

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your weight is: {round(weight)} {unit}")    
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight)} {unit}")
else:
    print(f"{unit} was not valid")