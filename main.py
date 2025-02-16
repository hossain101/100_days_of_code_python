# Ticket Counter : Nested if elif else statement

print("Welcome to the rollercoaster ride!!")
height = int(input("Enter your height in cm : "))
age = int(input("Enter your age in years : "))

if height >= 120:
    print("You are tall enough to ride the rollercoaster!!")
    if age >= 18:
        print("Your bill is $20")
    elif age >=12:
        print("Your bill is $15")
    else:
        print("Your bill is $10")
else:
    print("Get some inches in you before you can have a ride ")
