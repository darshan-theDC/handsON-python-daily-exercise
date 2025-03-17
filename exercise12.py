#print a rectangle

length = int(input("Enter the length of a rectangle : "))
breadth = int(input("Enter the breadth of a rectangle : "))
symbol = input("Enter the symbol used to print a rectangle : ")

for x in range(length):
    for y in range(breadth):
        print(symbol, end="")
    print()