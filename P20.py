as,by=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
h.reverse()
as=by
z=0
for i in h:
    if(as>=i):
        nm=int(as/i)
        z=z+n
        as=as-nm*i
    if as==0:
        break
if(as==0):
   print(z)
else:
     print("it's not posiible to select coins in such a way that they sum upto",S)  
