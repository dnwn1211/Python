N, X = map(int, input().split())
A = list(map(int, input().split()))

result = []
for num in A:
    if num < X:
        result.append(num)

print(*result)
