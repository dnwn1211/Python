#2839
#설탕 배달

k = int(input())

count = 0

for i in range((k // 5), 0, -1):
    sugar = k - (5 * i)
    if sugar % 3 == 0:
        count = i + (sugar // 3)
        print(count)
        break
else:
    print('-1')

    