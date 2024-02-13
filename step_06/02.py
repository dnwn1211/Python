chess = [1, 1, 2, 2, 2, 8]

chess_find = list(map(int, input().split()))

you_find = [str(chess[i] - chess_find[i]) for i in range(len(chess_find))]

print(' '.join(you_find))