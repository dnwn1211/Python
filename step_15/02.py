#13241

import math

def test(a,b):
  return abs(a*b)//math.gcd(a,b)

A,B=map(int, input().split())

print(test(A,B))