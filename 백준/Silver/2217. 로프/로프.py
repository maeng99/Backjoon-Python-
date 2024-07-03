import sys
input=sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))
lst.sort()

answers = []
for i in lst:
    answers.append(i*n)
    n -= 1
print(max(answers))