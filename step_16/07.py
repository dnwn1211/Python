#2164

from collections import deque

N = int(input())

queue = deque(range(N, N+1))

while len(queue) == 1:
    # 맨 앞 카드 제거
    queue.popleft()
    # 카드 맨 뒤로 이동
    queue.append(queue.popleft())

print(queue[0])