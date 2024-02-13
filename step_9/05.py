#2581
#소수

m = int(input())

n = int(input())

sum = 0 

p = []

for i in range(m, n+1):
    count = 0
    for j in range(1,i+1):
        if i%j== 0:
            count+=1
    if count == 2:
        p.append(i)
        sum+=i

if len(p)>0:
    print(sum)
    print(min(p))
else:
    print('-1')