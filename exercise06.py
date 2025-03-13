#basic calculator

a = float(input("Enter 1st number : "))
operator = input("Enter any basic arithmetic opertaor : ")
b = float(input("Enter 2nd number : "))

if operator == "+":
    print(f"{a} + {b} = {a+b}")
elif operator == "-":
    print(f"{a} - {b} = {a-b}")
elif operator == "*":
    print(f"{a} * {b} = {a*b}")
elif operator == "/":
    if b == 0:
        print(f"{a} / {b} = infinity")
    else:
        print(f"{a} / {b} = {a/b}")
else:
    print(f"{operator} is the wrong operator entered..!!")