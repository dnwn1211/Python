N, M = map(int, input().split())

baskets = list(range(1, N + 1))

for _ in range(M):

    i, j = map(int, input().split())

    i -= 1
    j -= 1

    baskets[i:j+1] = reversed(baskets[i:j+1])

print(*baskets)
