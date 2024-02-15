#2587
#대표값2

num = []

for _ in range(5):
    num.append(int(input()))
num.sort()
print(int(sum(num)/5))
print(num[len(num)//2])