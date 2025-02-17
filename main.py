# Ticket Counter : Nested if elif else statement with photo option

print("Welcome to the rollercoaster ride!!")
height = int(input("Enter your height in cm : "))
age = int(input("Enter your age in years : "))
bill = 0
if height >= 120:
    print("You are tall enough to ride the rollercoaster!!")
    if age >= 18:
        bill = 20

    elif age >= 12:
        bill = 15

    else:
        bill = 10

    want_photo = input("Photo on ride additional $3 (Y/N) : ")
    if want_photo.capitalize() == "Y":
        bill += 3
        print(f"Your Total Bill = {bill}")
    else:
        print(f"Your Total Bill = {bill}")
else:
    print("Get some inches in you before you can have a ride ")
