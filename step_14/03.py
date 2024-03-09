#7785

people = int(input())

people_log = set()

for i in range(people):
    name, status = input().split()
    if status == 'enter':
        people_log.add(name)
    else:
        people_log.remove(name)

for person_name in sorted(list(people_log), reverse=True):
    print(person_name)
