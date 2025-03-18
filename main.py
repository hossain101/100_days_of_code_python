# prime number checker


def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False

    if isPrime == True:
        print("Prime number")
    else:
        print("Not Prime number")


input_number = int(input("Enter a number: "))

prime_checker(number=input_number)
