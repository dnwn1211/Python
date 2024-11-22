#1010

import math

def fact(M, N):
    m = math.factorial(M)
    n = math.factorial(N)
    k = math.factorial(M - N)

    result = m // (n * k)
    return result

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())
    results.append(fact(M, N))

for result in results:
    print(result)
