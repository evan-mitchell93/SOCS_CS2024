#Evan Mitchell
#10/31/2024
#Determine if customer is old enough to purchase an R rated ticket.


age = int(input("Enter your age: "))

if age >= 18:
    if age >= 65:
        print("here is your discounted ticket")
    else:
        print("here is your ticket")
else:
    print("You cannot purchase a ticket")


name = input("Enter your name: ")

if name == "Jaden":
    print("Loser")