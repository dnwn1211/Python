#24313
#알고리즘 수업 - 점근적 표기 1

a1, a0 = map(int, input().split())

c = int(input())
n0 = int(input())

if abs(a0) <= abs(n0 * (c - a1)):
    print(1)
else:
    print(0)

