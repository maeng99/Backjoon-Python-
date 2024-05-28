import sys
input=sys.stdin.readline

n=int(input())
a, b = 0, 1

if n == 0:
  print(a)
  exit()
if n == 1:
  print(b)
  exit()
  
for _ in range(n-1):
  a, b = b, a+b

print(b)