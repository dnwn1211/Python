# 입력값 처리
n, m = map(int, input().split())

# 포켓몬 이름 -> 번호 딕셔너리
name_to_num = {}
# 포켓몬 번호 -> 이름 딕셔너리
num_to_name = {}

# 포켓몬 정보 입력
for i in range(1, n + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

# 문제 입력 및 처리
for _ in range(m):
    query = input().strip()
    if query.isdigit():  # 입력이 숫자인 경우
        print(num_to_name[int(query)])
    else:  # 입력이 문자 (포켓몬 이름)인 경우
        print(name_to_num[query])
