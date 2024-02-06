N, M = map(int, input().split())

matrix_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_A.append(row)

matrix_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_B.append(row)

for i in range(N):
    result_row = []
    for j in range(M):
        result_row.append(matrix_A[i][j] + matrix_B[i][j])
    print(' '.join(map(str, result_row)))
