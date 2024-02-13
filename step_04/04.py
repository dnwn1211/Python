numbers = [int(input()) for _ in range(9)]

max_value = numbers[0]
max_index = 1

for i in range(1, 9):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i + 1

print(max_value)
print(max_index)
