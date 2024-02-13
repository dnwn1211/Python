#9063
#대지

N = int(input())

x = []
y = []

for i in range(N):
    x_val, y_val = map(int, input().split())
    x.append(x_val)
    y.append(y_val)

if len(x) == 0 or len(y) == 0:
    print('0')
else:
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    square = (max_x - min_x) * (max_y - min_y)
    print(square)
