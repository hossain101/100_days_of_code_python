# Loops : random password generator
import random

print("Welcome to python password generator!!")

letter_n = int(input("How many letters would you like in your password? \n"))
symbol_n = int(input("How many symbols would you like in your password? \n"))
numbers_n = int(input("How many numbers would you like in your password? \n"))

# Character pools
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers_list = "0123456789"
symbol_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Start with an empty password string
password = ""

for char in range(1, letter_n + 1):
    password += random.choice(alphabets)

for char in range(1, symbol_n + 1):
    password += random.choice(symbol_list)
for char in range(1, numbers_n + 1):
    password += random.choice(numbers_list)

password_list = list(password)

print(password_list)

random.shuffle(password_list)

result = "".join(password_list)


print(result)
print(password)


print(f"password range = {letter_n + symbol_n + numbers_n}")
