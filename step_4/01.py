n = int(input())

arr = list(map(int, input().split()))

f = int(input())
count =0

for i in range(len(arr)):
    if(f==arr[i]):
        count +=1
print(count)
