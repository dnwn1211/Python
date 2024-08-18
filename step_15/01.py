#1934

import math

def lcm(a,b):
  return abs(a*b)//math.gcd(a,b)

T = int(input())

case = []

for _ in range(T):
  A, B = map(int,input().split())
  case.append(lcm(A,B))


for result in case:
  print(result)