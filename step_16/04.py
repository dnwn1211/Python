#4949

def check_balance(string):
    stack = []
    
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()

    if stack:
        return "no"
    else:
        return "yes"

# 입력 받기
while True:
    input_str = input()
    if input_str == ".":
        break
    print(check_balance(input_str))
