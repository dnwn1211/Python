#10815

n = int(input())

num1 = list(map(int, input().split()))

m = int(input())

num2 = list(map (int,input().split()))

result = []

card_set = set(num1)


for num in num2:
    if num in card_set:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))