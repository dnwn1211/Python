#2231
#분해합

n = int(input())

count =0

for i in range(1, n+1):
    n_sum = sum(map(int,str(i)))
    if i+n_sum == n:
        print(i)
        break
else:
    print('0')

