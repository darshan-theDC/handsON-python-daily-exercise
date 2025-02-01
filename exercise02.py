#shopping cart program
#ask to enter item, price, quantity

#approach : I've used input(), f statement and type coversion

item = input("Enter the item you want to purchase : ")
price = float(input("What is the price : "))
quantity = int(input("How many would you like to buy : "))

print(f"To buy {quantity} {item}, it will cost you Rs.{price*quantity}")