char = input().upper()

word_count = {}

for i in char:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

max_count = max(word_count.values())

max_chars = [k for k, v in word_count.items() if v == max_count]

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0])
