#14425

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input())

stringlist = []
for _ in range(M):
    stringlist.append(input())

count = 0
for string in stringlist:
    if string in S:
        count += 1

print(count)
