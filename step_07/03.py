lines = [input() for _ in range(5)]
word = ''
max_length = max(len(line) for line in lines)

for col in range(max_length):
    for row in range(5):
        if col >= len(lines[row]):
            continue
        word += lines[row][col]

print(word)
