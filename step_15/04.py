#2485

import math
from functools import reduce

def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)

N = int(input())
positions = [int(input()) for _ in range(N)]

gaps = [positions[i+1] - positions[i] for i in range(N-1)]

gcd_gap = gcd_multiple(gaps)

total_tree = sum((gap // gcd_gap) - 1 for gap in gaps)

print(total_tree)
