#17103

import sys
import math

def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    
    return is_prime

def goldbach_partitions(n, is_prime):
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1
    return count

input = sys.stdin.read
data = list(map(int, input().split()))

max_value = max(data[1:])


is_prime = sieve(max_value)

results = []
for n in data[1:]:
    results.append(goldbach_partitions(n, is_prime))

print("\n".join(map(str, results)))
