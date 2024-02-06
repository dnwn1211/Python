input_time = input()
value = input_time.split()
t1= int(value[0])
t2= int(value[1])

if t2-45<0:
    if t1-1<0:
        t1=23
        print(t1,t2+15)
    else:
        print(t1-1,t2+15)
elif t2-45==0:
    print(t1,t2-45)
elif t2-45>0:
    print(t1,t2-45)

