#1181
#단어정렬

n =  int(input())

char =[]

for _ in range(n):
    char.append(input())

char.sort(key=lambda x : (len(x),x))
sort_list=list(set(char))

for str in sort_list:
    print(str)