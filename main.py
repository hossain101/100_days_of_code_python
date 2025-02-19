# Bill Split game
import random

name_string = input("Please enter names of participants, separated by , and a space.\n")

name_list = name_string.split(", ")

random_index = random.randint(0, len(name_list) - 1)

print(f"{name_list[random_index]} will have to pay the bill.")
