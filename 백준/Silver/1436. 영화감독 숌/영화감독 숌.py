import sys

n=int(sys.stdin.readline().rstrip())

count=1
start=666

while True:
  if '666' in str(start):
    if count==n:
      print(start)
      break
    count+=1
  start+=1