ns,k=map(int,input().split())
ms=list(map(int,input().split()))
ms.sort()
ms.reverse()
sum=k
p=0
for i in ms:
    if(sum>=i):
        a=int(sum/i)
        p=p+a
        sum=sum-a*i
    if sum==0:
        break
if(sum==0):
   print(p)
else:
   print("it's not posiible to select coins in such a way that they sum upto",k)
