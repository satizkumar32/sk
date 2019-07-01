sk,h=input().split()
sk=int(sk)
h=int(h)
count=0
l=list(map(int,input().split()))
for i in range(sk):
    for j in range(i+1,sk):
        ss=0
        ss=l[i]+l[j]
        if(ss==h):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
