import sys
from collections import deque
input = sys.stdin.readline

t=int(input())

for _ in range(t):
  n,m=map(int,input().split())
  nl=list(map(int,input().split()))
  dq=deque(nl)
  rl=deque([0]*n)
  result=0
  rl[m]=1

  for _ in range(n):
    dq.rotate(-(nl.index(max(nl))))
    rl.rotate(-(nl.index(max(nl))))
  
    dq.popleft()
    r=rl.popleft()
    result+=1
    if r==1:
      print(result)
      break
    nl=list(dq)