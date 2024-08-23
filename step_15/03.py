#1735

import math

a, b = map(int, input().split())

c, d = map(int, input().split())

result1= a*d+c*b

result2= b*d

value=math.gcd(result1, result2)

result1//=value
result2//=value

print (result1, result2)