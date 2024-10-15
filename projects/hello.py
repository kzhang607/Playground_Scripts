#hypotenuse of a circle
import math 
a = float(input("What is the value of a: "))
b = float(input("What is the value of b: "))
hypotenuse = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse of the circle is {round(hypotenuse, 3)}")