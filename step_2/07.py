dice = list(map(int,input().split()))

def rollDice(dice):
    if len(set(dice))==1:
        return (10000+(dice[0]*1000))
    elif len(set(dice))==2:
        for num in set(dice):
            if dice.count(num) == 2:
                return (1000+(num*100))
    else:
        return (max(dice)*100)
result=rollDice(dice)
print(result)