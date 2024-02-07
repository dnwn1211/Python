n = int(input())

# 0~100 , 101
paper = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

black_area = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            black_area += 1

print(black_area)
