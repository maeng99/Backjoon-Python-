
import sys

input=sys.stdin.readline

t=int(input())
for _ in range(t):
  n=int(input())
  nl=[input().rstrip().split() for _ in range(n)]
  dict={}
  result=1
  
  for na,k in nl:
    if k not in dict:
      dict[k]=1
    else:
      dict[k]+=1
  lst=list(dict.values())

  for i in lst:
    result*=i+1
  print(result-1)