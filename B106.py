chan,chen=map(int,input().split())
lost=input().split()
chon=[]
for p in lost:
  if (int(p)%2!=0):
    chon.append(p)
print(chon[chen-1])
