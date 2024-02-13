input_time = input()
value = input_time.split()
t1= int(value[0])
t2= int(value[1])

t3=int(input())

if t3-60<=0:
    if t3+t2>=60:
        t1+=1
        if t1>=24:
            t1-=24
        print(t1,t2+t3-60)
    else:
        print(t1,(t2+t3))
elif t3-60>0:
    t1+=int((t2+t3)/60)
    if t1>=24:
        t1-=24
    print(t1,((t3+t2)%60))
