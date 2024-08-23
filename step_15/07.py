#4948

import sys
import math

def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    return sieve

def count_primes_in_range(n, sieve):
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            count += 1
    return count

input = sys.stdin.read
numbers = list(map(int, input().split()))

limit = 123456 * 2
sieve_list = sieve(limit)

for n in numbers:
    if n == 0:
        break
    print(count_primes_in_range(n, sieve_list))
