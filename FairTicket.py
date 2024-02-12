print("Welcome to the Fair Ticket Booth")
print("You must be atleast 60 inches tall to ride the roller coaster")
print("Ages 12 and under $5.00\nAges 13-17 $7.00\nAges 18 and up $10.00\n")
Age = int(input("What is your age? "))
Height = float(input("How tall are you in inches? "))

if Height >= 60:
    if Age <= 12:
        print("Your ticket will cost $5.00.")
    elif Age <= 17:
        print("Your ticket will cost $7.00.")
    else:
        print("Your ticket will cost $10.00.")
else:
    print("Sorry, you must be atleast 60 inches tall to ride the roller coaster.")