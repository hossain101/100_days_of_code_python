# Pizza Ordering system

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S,M,L : ").capitalize()

add_pepperoni = input("Do you want pepperoni?(Y/N) : ")
extra_cheese = input("Do you want extra cheese?(Y/N) : ")

total_bill = 0

if size == "S":
    total_bill += 15

elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2

    else:
        total_bill += 3


if extra_cheese == "Y":
    total_bill += 1


print(f"Your Total Bill is : ${total_bill}")
