import sys

input = sys.stdin.readline

t=int(input())

for _ in range(t):
  n=int(input())
  f=[[]]*(n+1)
  f[0]=[1, 0]
  if n>0:
    f[1]=[0, 1]
  
  for i in range(2, n+1):
    f[i]=[f[i-1][0]+f[i-2][0],f[i-1][1]+f[i-2][1]]

  print(*f[n])