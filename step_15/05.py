#4134

import math

def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_next_prime(n):
    while not prime(n):
        n += 1
    return n

T = int(input())

for _ in range(T):
    n = int(input())
    print(find_next_prime(n))
