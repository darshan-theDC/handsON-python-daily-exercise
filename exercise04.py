#calculate circumference and area of the circle

import math

radius = float(input("Enter the radius : "))

print(f"Circumference of the circle : {round(2*math.pi*radius, 2)}cm")
print(f"Area of the circle : {round(math.pi*(radius**2), 2)}sq.cm.")