n, b = map(int, input().split())

change =''

while n > 0:
    replace = n % b
    if replace >= 10:
        change = chr(replace - 10 + ord('A')) + change
    else:
        change = str(replace) + change
    n //= b

print(change)
