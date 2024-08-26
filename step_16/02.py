# 10773

K = int(input())

array=[]

for _ in range(K):
  N = int(input())
  if N == 0:
    array.pop()
  else: 
    array.append(N)

print(sum(array))