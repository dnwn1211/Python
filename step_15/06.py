#1929

#에라토스테네스의 체의 소수 알고리즘
def find_prime(num):
  prime = [True] * (num + 1)
  prime[0] = prime[1] = False  # 0과 1은 소수가 아니므로 False로 설정
    
  for i in range(2, int(num ** 0.5) + 1):
    if prime[i]:  # i가 소수이면
      for j in range(i * i, num + 1, i):
        prime[j] = False  # i의 배수를 제거
    
  return prime

M, N = map(int, input().split())

prime = find_prime(N)

for i in range(M, N + 1):
    if prime[i]:
        print(i)