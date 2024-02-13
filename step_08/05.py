N = int(input())

if N == 1:
    print(1)
else:
    count = 1
    num = 1
    d = 6

    while num < N:
        num += d
        d += 6
        count += 1

    print(count)
