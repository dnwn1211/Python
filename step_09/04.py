#1978
#소수 찾기

x = int(input())
num_list = list(map(int, input().split()))

count = 0
for i in num_list:
    error = 0
    if i > 1:    
        for j in range(2, i):
            if i%j == 0:
                error += 1
        if error == 0:
            count += 1
          
print(count)