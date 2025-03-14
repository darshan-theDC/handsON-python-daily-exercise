#validate user input
#1. username should not have more than 12 characters
#2. username must not contain any spaces
#3. username must not contain digits

username = input("**USERNAME ENTRY**\n1. Username should not have more than 12 characters\n2. Username must not contain any spaces\n3. Username must not contain digits\nEnter username : ")

if len(username) > 12:
    print(f"{username} is a invalid username!, it cannot contain more than 12 character....")
elif not username.isalpha():
    print(f"{username} is a invalid username!, it acnnot contain any spaces")
elif username.isdigit():
    print(f"{username} is a invalid username!, it cannot contain any digits")
else:
    print(f"{username} is a valid username!")