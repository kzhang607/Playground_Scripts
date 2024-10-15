#calculator program
operator = input("Please select an operator(+,-,*,/): ")
number_1 = float(input("Please enter your first number: "))
number_2 = float(input("Please enter your second number: "))
if operator == "+":
    final_number = number_1 + number_2
    print(f"Your calculation is: {round(final_number,3)}")
elif operator == "-":
    final_number = round(number_1-number_2, 3)
    print(f"Your calculation is: {round(final_number,3)}")
elif operator == "*":
    final_number = round(number_1*number_2, 3)
    print(f"Your calculation is: {round(final_number,3)}")
elif operator == "/":
    final_number = round(number_1/number_2, 3)
    print(f"Your calculation is: {round(final_number,3)}")
else:
    print(f"Your {operator} is not a valid operator and neither are you")

