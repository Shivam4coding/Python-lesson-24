from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(sqrt(number))
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

