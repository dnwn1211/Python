#10989
#수 정렬하기 3
import sys

count = [0] * 10001

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i) + '\n')

