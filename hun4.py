p=int(input())
pq=list(map(int,input().split()))
cp=[]
for i in apa:
  if(pq.count(i)>1):
    cp.append(i)
  else:
    print(i)
