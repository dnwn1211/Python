#2750
#수 정렬하기

n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))

num.sort()

for i in range(len(num)):
    print(num[i])