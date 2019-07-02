lis=[int(i) for i in input().split()]
l=lis[0]
b=lis[1]
h=lis[2]
sa=2*((l*b)+(b*h)+(l*h))
vol=l*b*h
print(sa,vol)
