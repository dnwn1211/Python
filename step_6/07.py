N = int(input()) 
count = 0

for _ in range(N):
    word = input()
    char_set = set()
    is_group_word = True
    
    prev_char = ''
    for char in word:
        if char != prev_char:
            if char in char_set:
                is_group_word = False
                break
            char_set.add(char) 
            prev_char = char 
        else:
            continue
    
    if is_group_word:
        count += 1

print(count)
