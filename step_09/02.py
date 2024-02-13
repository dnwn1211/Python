# 2501

n, k = map(int, input().split())

count = 0
result = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        if count == k:
            result = i
            break

if count >= k:
    print(result)
else:
    print(0)
