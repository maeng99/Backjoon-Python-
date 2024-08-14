import sys

#해당 간선이 사이클을 발생시키는지 확인하기 위해 실행하는 함수
#parent배열을 통해 x의 부모를 재귀적으로 찾는 함수
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#사이클이 발생되지 않아, 최소신장트리에 해당 간선 포함할 때 실행하는 함수
#parent배열을 업데이트 시켜 해당 노드의 부모 노드를 저장하는 함수 
def union_parent(parent,a,b): 
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 수
v=int(sys.stdin.readline().rstrip())
#간선의 수
e=int(sys.stdin.readline().rstrip())

parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int, sys.stdin.readline().split())
    edges.append((cost,a,b))

#간선을 오름차순으로 정렬
edges.sort()

for edge in edges:
    cost,a,b=edge
    #해당 간선이 사이클을 발생시키는지 확인 후, 발생시키지 않는다면 최소신장트리에 포함시킨다.
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        #result에 cost(가중치)를 더해줌으로써 최소비용을 업데이트 시킨다.
        result+=cost

print(result)