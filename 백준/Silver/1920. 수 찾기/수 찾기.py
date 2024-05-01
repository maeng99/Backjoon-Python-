import sys

n=int(sys.stdin.readline().rstrip())
nl=set(map(int, sys.stdin.readline().rstrip().split()))

m=int(sys.stdin.readline().rstrip())
ml=map(int, sys.stdin.readline().rstrip().split())


for i in ml:
  if i in nl:
    print(1)
  else:
    print(0)