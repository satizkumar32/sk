vjs=int(input())
v=list()
for i in range(vjs):
    b=input().split()
    b=[int(d) for d in b]
    for j in b:
        v.append(j)
v.sort()
for i in v:
    print(i,end=" ")
