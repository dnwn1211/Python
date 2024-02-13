#14215
#세 막대

tri = list(map(int,input().split()))

tri.sort()

while True : 
    if tri[0]+tri[1]<=tri[2]:
        tri[2]-=1
    else:
        print(sum(tri))
        break