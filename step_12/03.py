#19532
#수학은 비대면강의입니다

import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
det = a*e - b*d
if det != 0:
    x = (c*e - b*f) / det
    y = (a*f - c*d) / det
    print(int(x), int(y))
else:
    print(" ")