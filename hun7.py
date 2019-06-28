    
aa=int(input())
bb=list(map(int,input().split()))
l=[]
for i in range(0,len(bb)):
    if bb[i]%2==0 and i%2==1:
        l.append(bb[i])
    elif bb[i]%2==1 and i%2==0:
        l.append(bb[i])
print(*l,sep=' ')
