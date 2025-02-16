# BMI Calculator

print("Welcome to BMI calculator")

height = float(input("What is your height in m2 : "))
weight = float(input("What is your weight in KG : "))

BMI = round(weight/height**2)
print(f"Your BMI : {BMI}")
if BMI<18.5:
    print("You are underweight")
elif BMI<25:
    print("You have normal weight")
elif BMI<30:
    print("You are overweight")
elif BMI<35:
    print("You are obese")
else:
    print("You are clinically obese")





