import sys

input=sys.stdin.readline


n,m=map(int,input().split())
poket=[input().rstrip() for _ in range(n)]
ques=[input().rstrip() for _ in range(m)]
result=[]

for q in ques:
  if q.isdigit():
    result.append(poket[int(q)-1])
  else:
    result.append(poket.index(q)+1)

for i in result:
  print(i)