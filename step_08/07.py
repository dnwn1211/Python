up, down, tree = map(int, input().split())

height = (tree - up) // (up - down)
remaining = (tree - up) % (up - down)

if remaining == 0:
    print(height + 1)
else:
    print(height + 2)
