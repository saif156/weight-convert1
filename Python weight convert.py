#Python weight convert

weight=float(input("Enter your weight: ") )
unit=input("Kilogram or Pounds? (K or L): ")

if unit == "K" :
    weight  = weight*2.205
    unit = "lbs. "
elif unit == "L" :
    weight = weight/2.205
    unit = "Kgs. "
else:
    print(f"{unit} was not valid")

print(f"your weight is: {weight}{unit}")