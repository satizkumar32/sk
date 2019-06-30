from itertools import combinations
ns,n2=input().split()
n2=int(n2)
l=[]
dd=combinations(n,len(ns)-n2)
for i in list(dd):
  l.append("".join(i))
print(min(l))
