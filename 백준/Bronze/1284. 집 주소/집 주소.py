import sys

input=sys.stdin.readline

while True:
  n=input().rstrip()
  nsum=0
  if n=='0':
    break
  for i in range(len(n)):
    if n[i]=='0':
      nsum+=4
    elif n[i]=='1':
      nsum+=2
    else:
      nsum+=3
  print(nsum+len(n)+1)