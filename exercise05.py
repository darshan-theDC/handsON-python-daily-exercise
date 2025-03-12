#find hypotenuse of the right triangle

import math

a = int(input("Enter the opposite length : "))
b = int(input("Enter the adjacent length : "))

print(f"Hypotenuse length of the right triangle is {round(math.sqrt(math.pow(a,2)+math.pow(b,2)))}")