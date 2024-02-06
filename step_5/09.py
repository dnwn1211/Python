num = input().split()

reversed_numbers = [int(number[::-1]) for number in num]

max_number = max(reversed_numbers)

print(max_number)
