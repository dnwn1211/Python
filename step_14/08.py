#11478

def diff(s):
    substrings = set()
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])

    return len(substrings)

s = input()
result = diff(s)
print(result)