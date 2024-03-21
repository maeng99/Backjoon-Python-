# 시간초과로 인해 dictionary 사용

import sys

input=sys.stdin.readline

n,m=map(int,input().split())
nl=[input().rstrip() for _ in range(n)]
ml=[input().rstrip() for _ in range(m)]
dict={}
dict2={}

for i in nl:
  dict[i]=1
for i in ml:
  if i in dict:
    dict2[i]=1
dict2=sorted(dict2.keys())
print(len(dict2))
for i in dict2:
  print(i)