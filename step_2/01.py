input_num = input()
value= input_num.split()

A=int(value[0])
B=int(value[1])

if A>B:
    print('>')
elif A<B:
    print('<')
elif A==B:
    print('==')