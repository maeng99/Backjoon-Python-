t=int(input())
type=[300, 60, 10]
result=[]

for i in type:
  result.append(t//i)
  t%=i
if t!=0:
  print(-1)
else:
  for i in range(len(result)):
    print(result[i], end=" ")