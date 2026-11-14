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

print("Two-digit prime numbers are:")

for num in range(10, 100):
    if is_prime(num):
        print(num, end=" ")