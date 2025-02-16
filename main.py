# Leap Year Calculator

print("Welcome to leap year calculator")

year = int(input("Enter the year you wish to check : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")

        else:
            print("not A leap year")
    else:
        print("a leap year")
else:
    print(" Not a Leap Year")
