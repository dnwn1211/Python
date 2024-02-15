#11650
#좌표 정렬하기

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()

for point in points:
    print(point[0], point[1])

