submitted = set(int(input()) for _ in range(28))

all_students = set(range(1, 31))

not_submitted = sorted(all_students - submitted)

print(not_submitted[0])
print(not_submitted[1])
