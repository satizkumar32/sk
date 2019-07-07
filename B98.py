sk1=int(input())
sat1=list(map(int,input().split()))
for p in range(len(sat1)-1):
     if(sat1[p]>sat1[p+1]):
           print(p)
           break
