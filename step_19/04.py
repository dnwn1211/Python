#11050

import math

N, K = map(int, input().split())

def fact(N, K):
    n = math.factorial(N)
    k = math.factorial(K)
    z = math.factorial(N-K)
    result = n//(k*z)
    
    return result

print(fact(N, K))