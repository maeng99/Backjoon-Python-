import sys

input = sys.stdin.readline

n = int(input())
tL, pL = [], []
for _ in range(n):
  t, p = map(int, input().split())
  tL.append(t)
  pL.append(p)
total = [0] * n

if tL[n - 1] == 1:
  total[n - 1] = pL[n - 1]
  if n == 1:
    print(total[0])
    exit()

for i in range(n - 2, -1, -1):
  if i + tL[i] > n:
    total[i] = 0
    for x in range(i + 1, n):
      total[i] = max(total[i], total[x])
  else:
    if i + tL[i] <= n - 1:
      total[i] = max(total[i + 1], pL[i] + total[i + tL[i]])
    else:
      total[i] = max(total[i + 1], pL[i])
print(total[0])
