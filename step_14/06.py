#1764

N, M =map(int, input().split())

heard=set()
for i in range(N):
  heard.add(input().strip())

seen=set()
for j in range(M):
  seen.add(input().strip())

heard_seen=sorted(heard&seen)

print(len(heard_seen))
for name in heard_seen:
  print(name)