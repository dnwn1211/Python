#28279

from collections import deque
import sys
input = sys.stdin.readline

d = deque()
output = []

N = int(input().strip())  # 괄호 () 추가

for _ in range(N):
    command = input().strip().split()

    if command[0] == '1':       # 1 X: 덱의 앞에 X 추가
        d.appendleft(int(command[1]))
    elif command[0] == '2':     # 2 X: 덱의 뒤에 X 추가
        d.append(int(command[1]))
    elif command[0] == '3':     # 3: 덱의 맨 앞 정수 빼고 출력
        output.append(d.popleft() if d else -1)
    elif command[0] == '4':     # 4: 덱의 맨 뒤 정수 빼고 출력
        output.append(d.pop() if d else -1)
    elif command[0] == '5':     # 5: 덱의 정수 개수 출력
        output.append(len(d))
    elif command[0] == '6':     # 6: 덱이 비어있는지 확인
        output.append(1 if not d else 0)
    elif command[0] == '7':     # 7: 덱의 맨 앞 정수 출력
        output.append(d[0] if d else -1)
    elif command[0] == '8':     # 8: 덱의 맨 뒤 정수 출력
        output.append(d[-1] if d else -1)

# 한 번에 출력
print("\n".join(map(str, output)))
