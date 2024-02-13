#10101
#삼각형 외우기

t1 = int(input())
t2 = int(input())
t3 = int(input())

sum = t1+t2+t3

if sum != 180:
    print('Error')
else:
    if t1 == t2:
        print('Isosceles')
    elif t1 == t3:
        print('Isosceles')
    elif t2 == t3:
        print('Isosceles')
    elif t1==t2==t3:
        print('Isosceles')
    else:
        print('Scalene')