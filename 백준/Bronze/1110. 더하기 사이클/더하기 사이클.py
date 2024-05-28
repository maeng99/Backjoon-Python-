import sys
input=sys.stdin.readline

s=input()
s_new=s
if int(s)//10 == 0:
  sl = int(s)
else:
  sl=int(s[0])+int(s[1])
cnt=1

while True:
  s_new = str(int(s_new)%10) + str(sl%10)
  if int(s) == int(s_new):
    print(cnt)
    exit()
  sl = int(s_new[0])+int(s_new[1])
  cnt+=1