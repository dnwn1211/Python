#12789

def can_snack(N, students):
    stack = []
    snack = 1  # 1번부터 순서대로 간식을 받아야 함

    for student in students:
        # 대기열의 학생을 스택으로 보냄
        while stack and stack[-1] == snack:
            stack.pop()
            snack += 1
        
        if student == snack:
            snack += 1
        else:
            # 바로 받을 수 없으면 스택에 저장
            stack.append(student)
    
    # 마지막으로 스택에 남은 학생들 중에서 순서대로 받을 수 있는지 확인
    while stack and stack[-1] == snack:
        stack.pop()
        snack+= 1

    # 모든 학생이 순서대로 간식을 받았으면 "Nice", 아니면 "Sad" 출력
    return "Nice" if not stack else "Sad"


N = int(input())
students = list(map(int, input().split()))

print(can_snack(N, students))
