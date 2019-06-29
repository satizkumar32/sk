sk=int(input())
srr=list(map(int,input().split()[:sk]))
srm=sorted(srr)
for i in srm:
    print(i,end=" ")
