#28278

import sys
input = sys.stdin.read

def stack_operations(operations):
    stack = []
    output = []
    
    for operation in operations:
        if operation[0] == '1': 
            stack.append(int(operation[1]))
        elif operation[0] == '2': 
            if stack:
                output.append(stack.pop())
            else:
                output.append(-1)
        elif operation[0] == '3':  
            output.append(len(stack))
        elif operation[0] == '4': 
            output.append(1 if not stack else 0)
        elif operation[0] == '5': 
            if stack:
                output.append(stack[-1])
            else:
                output.append(-1)
    
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

input_data = input().splitlines()

n = int(input_data[0])

operations = [line.split() for line in input_data[1:n+1]]
stack_operations(operations)
