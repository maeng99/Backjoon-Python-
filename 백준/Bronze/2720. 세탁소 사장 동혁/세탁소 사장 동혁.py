t=int(input())
case=[]
list=[25, 10, 5, 1]

for _ in range(t):
  n=int(input())
  case.append(n)
  
for i in case:
  for j in list:
    result=i//j
    print(result, end=" ")
    remain=i%j
    i=remain
  print()
   