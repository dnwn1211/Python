n = int(input())

for _ in range(n):
    
    C = int(input())

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while C > 0:
        if C >= 25:
            quarters += 1
            C -= 25
        elif C >= 10:
            dimes += 1
            C -= 10
        elif C >= 5:
            nickels += 1
            C -= 5
        else:
            pennies += 1
            C -= 1

    # 결과 출력
    print(quarters, dimes, nickels, pennies)
