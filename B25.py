sk=int(input())
lsk=list(map(int,input().split()))
lsk.sort()
g=lsk[int(sk/2)]
print(g)
