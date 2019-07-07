jjj,hhh=map(int,input().split())
ff=list(map(int,input().split()[:hh]))
kk=[]
for i in ff:
   if(i<=i+1):
     kk.append(i)
print(kk[hhh-1])
