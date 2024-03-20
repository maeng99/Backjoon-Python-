import sys

input=sys.stdin.readline


m=int(input())
cl=['1','2','3']

for _ in range(m):
  x,y=input().rstrip().split()
  xi, yi=cl.index(x), cl.index(y)
  cl[xi], cl[yi]=y, x

print(cl[0])