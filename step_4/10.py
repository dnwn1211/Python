n = int(input())

point = list(map(int, input().split()))

good = max(point)

total = 0
for i in range(n):
    point[i] = point[i] / good * 100
    total += point[i]

# 평균을 계산하여 출력합니다.
avg = total / n
print(avg)
