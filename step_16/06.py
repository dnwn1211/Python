#18258

from collections import deque
import sys
input = sys.stdin.read

# 큐 초기화
queue = deque()

# 입력받기
data = input().strip().splitlines()
N = int(data[0])
commands = data[1:N + 1]

# 명령 처리
result = []
for command in commands:
    if command.startswith("push"):
        _, value = command.split()
        queue.append(int(value))
    elif command == "pop":
        result.append(queue.popleft() if queue else -1)
    elif command == "front":
        result.append(queue[0] if queue else -1)
    elif command == "back":
        result.append(queue[-1] if queue else -1)
    elif command == "size":
        result.append(len(queue))
    elif command == "empty":
        result.append(0 if queue else 1)

# 결과 출력
print("\n".join(map(str, result)))
