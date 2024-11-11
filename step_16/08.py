#11866

from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N + 1))
result = []

while people:
    # k-1명 뒤로 보내기
    people.rotate(-(K - 1))
    # K번째 사람 제거하고 새로운 배열에 추가
    result.append(people.popleft())

# 제거한 배열 출력
print("<" + ", ".join(map(str, result)) + ">")
