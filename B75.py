gs=list(input())
if len(gs)%2==0:
    gs[int(len(gs)/2)] ='*'
    gs[int(len(gs)/2)-1]='*'
else:
    gs[int(len(gs)/2)] ='*'
for i in range(0,len(gs)):
    print(gs[i],end='')
