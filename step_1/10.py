A = int(input())
B = input()

B_digits = [int(digit) for digit in B]

result_2 = A * B_digits[2]
result_1 = A * B_digits[1]
result_0 = A * B_digits[0]
result_total = A * int(B)

print(result_2)
print(result_1)
print(result_0)
print(result_total)
