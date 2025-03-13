#temperature conversion

temp = float(input("Enter the temperature : "))
unit = input("Enter the unit (Celcius - C / Fahrenheit - F) : ")

if unit == "C":
    print(f"Temperature in Fahrenheit is {round((temp*9/5)+32, 2)} F")
elif unit == "F":
    print(f"Temperature in Celius is {round((temp-32)*5/9, 2)} C")
else:
    print(f"{unit} is the invalid unit of temperature")