ug=int(input())
ul=list(map(int,input().split()))
us=[]
for i in ul:
    if(i==ul.index(i)):
        us.append(i)
print(*(sorted(us)))
if(len(us)==0):
    print(-1)
