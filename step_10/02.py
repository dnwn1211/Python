#1085
#직사각형에서 탈출

x,y,w,h = map(int, input().split())

m = []

m.append(x)
m.append(w-x)
m.append(y)
m.append(h-y)

print(min(m))