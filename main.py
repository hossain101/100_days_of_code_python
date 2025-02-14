# Tip Calculator.

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill ? \n"))
percentage_tip = int(input("What percentage of tip would you like to give? 10, 12, 0r 15? \n"))
people_split = int(input("How many people to split the bill? \n"))

split_bill = total_bill * (1+ percentage_tip/100) /people_split

print(f"Each person should pay : ${round(split_bill,2)}")

