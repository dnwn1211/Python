N = int(input())

end_of_world = 666
count = 0

while True:
    if '666' in str(end_of_world):
        count += 1
        # print(end_of_world)
        if count == N:
            print(count)
            # print(end_of_world)
            break
    end_of_world += 1
    print(end_of_world)

