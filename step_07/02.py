max_value = 0
max_row = 1
max_col = 1

for i in range(9):
    row = [int(i) for i in input().split()]
    for j in range(9):
        if row[j] > max_value:
            max_value = row[j]
            max_row = i + 1
            max_col = j + 1
print(max_value)
print(max_row, max_col)
