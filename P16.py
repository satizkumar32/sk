abc=int(input())
cd=list(map(int,input().split()))
xy=[1]*abc
for i in range(abc):
    if i==0:
        if cd[i]>cd[i+1]:
            xy[i]=xy[i]+xy[i+1]
    elif i>0:
        if cd[i]>cd[i-1]:
            xy[i]=xy[i]+xy[i-1]
print(sum(xy))
