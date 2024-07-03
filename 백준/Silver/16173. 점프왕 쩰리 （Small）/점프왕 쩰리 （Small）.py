import sys
input=sys.stdin.readline

n=int(input())

m=[]
for _ in range(n):
  m.append(list(map(int, input().split())))
a=0

def dfs(x, y):
  global a
  if x>=n or y>=n:
    return
  if m[x][y]==0:
    return
  if m[x][y]==-1:
    a+=1
    return
  dfs(x+m[x][y],y)
  dfs(x,y+m[x][y])

dfs(0, 0)
if a>=1:
  print("HaruHaru")
else:
  print("Hing")