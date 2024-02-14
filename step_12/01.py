#2798
#블랙잭

n, m = map(int, input().split())

card = list(map(int, input().split()))[:n]

sum_card = 0

for i in range (n-2):
    for j in range (i+1, n-1):
        for z in range (j+1, n):
            sum = card[i]+card[j]+card[z]
            if sum<=m and sum> sum_card:
                sum_card= sum
print(sum_card)
