#weight convertor

weight = float(input("Enter your weight : "))
unit = input("Enter the unit (kg/lbs) : ")

if unit == "kg":
    print(f"Your weight is : {weight*2.205}lbs")
elif unit == "lbs":
    print(f"Your weight is : {weight/2.205}kg")
else :
    print(f"{unit} is the invalid unit of weight")