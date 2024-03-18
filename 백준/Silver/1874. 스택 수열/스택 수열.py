from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
nl=deque()
pushorpop=[]
stack=[]

for _ in range(n):
  nl.append(int(input()))

for i in range(1,n+1):
  stack.append(i)
  pushorpop.append('+')
  if stack[-1] == nl[0]:
    while stack[-1]==nl[0]:
      stack.pop()
      nl.popleft()
      pushorpop.append('-')
      if len(stack)==0:
        break
  
if len(stack)!=0:
  print('NO')
else:
  for i in pushorpop:
    print(i)