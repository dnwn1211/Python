n, m = map(int, input().split())

max_chess_changes = 64  # 8x8 체스판에서 각 칸마다 최대로 다시 칠할 수 있는 횟수

count = max_chess_changes  # 충분히 큰 값으로 초기화

chess = []

for _ in range(n):
    row = input().strip()  # 문자열 입력 받고 좌우 공백 제거
    chess.append(list(row))  # 한 글자씩 나눠서 리스트에 추가

# 모든 가능한 8x8 체스판을 탐색
for i in range(n - 7):
    for j in range(m - 7):
        # 각 체스판의 시작 색깔이 'W'일 때와 'B'일 때를 고려
        for start_color in ['W', 'B']:
            current_count = 0
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    # 현재 칸이 정답 체스판과 다르다면 count 증가
                    if chess[x][y] != ((x + y) % 2 == 0 and start_color or chr(87 - ord(start_color))):
                        current_count += 1
            # 최솟값 갱신
            count = min(count, current_count)

print(count)
