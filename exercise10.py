#compound interest calculator

principle, rate, time = 0, 0, 0

while True:
    principle = float(input("Enter the priciple amount : "))
    if principle <= 0:
        print("Amount cannot be under Rs.0")
    else:
        break

while True:
    rate = float(input("Enter the rate : "))
    if rate == 0:
        print("Interest rate can't be zero")
    else:
        break

while True:
    time = float(input("Enter the time required : "))
    if time == 0:
        print("Time required cannot be zero")
    else:
        break

final_amount = principle * pow((1+rate/100),time)

print(f"The final amount that needs to be payed for Rs.{principle} in {time} years within coumpound interest {rate}% is Rs.{final_amount:.2f}")