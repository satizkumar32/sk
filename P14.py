vjs,vk=map(int,input().split())
ls=list(map(int,input().split()))
vjs=[]
ls.insert(0,0)
for y in range(vk):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=ls[i]     
     vjs.append(sumup)
for y in vjs:
    print(y)
