#weight converter
weight = float(input("Enter your weight: "))
unit = (input("What is your unit of measurement?(lb/kg): "))
if unit == "kg":
    weight = weight * 2.205
    print(f"Your weight in lbs is {round(weight, 3)}")
elif unit == "lb":
    weight = weight / 2.205
    print(f"Your weight in kgs is {round(weight, 3)}")
else:
    print(f"Your unit of {unit} is not valid.")
