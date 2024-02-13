#3009
#네 번째 점

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = [x1, x2, x3]
y = [y1, y2, y3]

for i in x:
    if x.count(i) == 1:
        x4 = i
        break

for j in y:
    if y.count(j) == 1:
        y4 = j
        break

print(x4, y4)
