import sys

input=sys.stdin.readline

n,m=map(int,input().split())
nl=dict(input().rstrip().split() for _ in range(n))
ml=[input().rstrip() for _ in range(m)]
result=[]

for i in ml:
  print(nl[i])