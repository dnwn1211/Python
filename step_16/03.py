#9012

T = int(input())

for _ in range(T):
    vps = input()
    count = 0
    ok_vps = True

    for char in vps:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            ok_vps = False
            break

    if count != 0:
        ok_vps = False

    if ok_vps:
        print("YES")
    else:
        print("NO")