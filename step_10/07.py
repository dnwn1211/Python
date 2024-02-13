#5073
#삼각형과 세 변

while True: 
    tri = list(map(int, input().split()))
    tri.sort()
    print(tri)

    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break

    if tri[0] + tri[1] <= tri[2]:
        print('Invalid')

    elif tri[0] == tri[1] == tri[2]:
        print('Equilateral')

    elif tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]:
        print('Isosceles')

    else:
        print('Scalene')

