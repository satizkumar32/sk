qs=int(input())
hs=list(map(int,input().split()))
os=max(hs)
xx,yy=0,0
for i in range(0,len(hs)-1):
  for j in range(i+1,len(hs)):
    if ab(hs[i]+hs[j])<os:
      xx,yy=hs[i],hs[j]
      os=ab(xx+yy)
print(x,y)
