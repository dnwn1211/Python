while True:
    try:
        a, b = map(int, input().split())
        
        if a > 0 and b > 0:
            print(a + b)
        
        elif a == 0 and b == 0:
            break
        
    except EOFError:
        break