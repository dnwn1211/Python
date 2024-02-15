#10814
#나이순 정렬

n = int(input())

people = []

for _ in range(n):
    age, name = input().split()
    people.append((int(age), name))

people.sort(key=lambda x: x[0])

for info in people:
    print(info[0], info[1])

