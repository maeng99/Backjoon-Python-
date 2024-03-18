import sys
input = sys.stdin.readline

n,m,b=map(int, input().split())
gl=[]
min_time=500*500*256*2
ground=0

for _ in range(n):
  gl.append(list(map(int, input().split())))

gmin=min(gl[0])
gmax=max(gl[0])

for i in range(1,n):
  if gmin>min(gl[i]):
    gmin=min(gl[i])
  if gmax<max(gl[i]):
    gmax=max(gl[i])

for k in range(gmin, gmax+1):
  time=0
  inven=b
  for i in gl:
    for j in i:
      if k-j>=0:
        time+=k-j
        inven-=k-j
      else:
        time+=abs(k-j)*2
        inven+=abs(k-j)
  if inven<0:
    continue
  if time<=min_time:
    min_time=time
    ground=k

print(min_time, ground)