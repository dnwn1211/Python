n = int(input())
basic =2
point =0

for _ in range (n):
    basic=basic+(basic-1)
    point = (pow(basic,2))

print (point)