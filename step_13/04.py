#2751
#수 정렬하기 2
import sys

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for _ in range(n)]

num.sort()

for i in num:
    sys.stdout.write(str(i) + '\n')

