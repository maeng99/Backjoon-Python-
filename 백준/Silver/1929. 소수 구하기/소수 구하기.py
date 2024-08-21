import sys
import math

m,n=map(int,sys.stdin.readline().rstrip().split())
nl=[]

for i in range(m,n+1):
  if i<=1:
    continue
  c=True
  for j in range(2, int(math.sqrt(i))+1):
    if i%j==0:
      c=False
      break
  if c:
    print(i)