#1269

n,m = map(int, input().split())

A = set(list(map(int, input().split())))

B= set(list(map(int, input().split())))

AmB = list(A-B)

BmA = list(B-A)

sum = len(AmB)+len(BmA)

print(sum)