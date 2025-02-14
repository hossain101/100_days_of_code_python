# Age remaining calculator.

current_age=int( input("What is your current age? \n"))
years_remaining= 90-current_age

weeks_remaining = years_remaining * 57
days_remaining = years_remaining  * 365
months_remaining = years_remaining *12


print(f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks & {days_remaining} days left.  Have Fun!!")


