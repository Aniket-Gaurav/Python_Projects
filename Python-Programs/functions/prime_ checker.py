import math


def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2, math.ceil(number) + 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")


n = int(input("Enter a number: "))
prime_checker(n)
