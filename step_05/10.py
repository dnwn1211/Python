alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

char = input()

char = char.upper()

total = 0

for i in range(len(char)):
    if char[i] in alpha[0:3]:
        total += 3
    elif char[i] in alpha[3:6]:
        total += 4
    elif char[i] in alpha[6:9]:
        total += 5
    elif char[i] in alpha[9:12]:
        total += 6
    elif char[i] in alpha[12:15]:
        total += 7
    elif char[i] in alpha[15:19]:
        total += 8
    elif char[i] in alpha[19:22]:
        total += 9
    elif char[i] in alpha[22:26]:
        total += 10

print(total)
