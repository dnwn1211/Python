total=int(input())
count=int(input())

totalresult=0

for _ in range(count):
    p1, p2=map(int, input().split())
    totalresult+=(p1*p2)
    
if totalresult==total:
    print("Yes")
else:
    print("No")
