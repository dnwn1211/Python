#11653 
#소인수분해

N = int(input())
i = 2
arr = []

while i <= N:
    if N % i == 0:
        arr.append(i)
        N /= i
    else:
        i += 1

for num in arr:
    print(num)

