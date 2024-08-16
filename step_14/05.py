from collections import Counter

# 입력 받기
N = int(input())
number_card = list(map(int, input().split()))

M = int(input())
find_number = list(map(int, input().split()))

# 숫자 카드의 개수를 셉니다.
card_count = Counter(number_card)

# 각 숫자가 몇 개 있는지 출력합니다.
result = []
for num in find_number:
    result.append(str(card_count[num]))

print(' '.join(result))
