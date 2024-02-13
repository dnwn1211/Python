alphabet = 'abcdefghijklmnopqrstuvwxyz'

char = input()

for ch in alphabet:
    if ch in char:
        print(char.index(ch), end=' ')
    else:
        print(-1, end=' ')
