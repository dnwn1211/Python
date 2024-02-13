# 9506
# 약수들의 합

while True:
    n = int(input())
    arr = []

    if n == -1:
        break
    
    for i in range(1,(n//2)+1):
        if n % i == 0 :
            arr.append(i)

    if n == sum(arr) :
        div = ' + '.join(map(str, arr))
        print(f'{n} = {div}')
    else:
        print(f'{n} is NOT perfect.')
 
