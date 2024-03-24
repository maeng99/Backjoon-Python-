# 규칙을 찾아버림

import sys

input = sys.stdin.readline

t=int(input())

for _ in range(t):
  n=int(input())
  f=[0]*(n+3)
  f[0], f[1], f[2]=1, 2, 4

  for i in range(3, n):
    f[i]=f[i-1]+f[i-2]+f[i-3]

  print(f[n-1])