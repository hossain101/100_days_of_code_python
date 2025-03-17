#No of cans of paint
import math
height = int(input("Enter your height in metres: "))
width = int(input("Enter your width in metres: "))


def pait_calc(height=height, width=width, coverage=5):
    no_can = math.ceil(((height * width) / coverage))
    print(f"No of cans required : {no_can}")


pait_calc()
