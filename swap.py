mash=input()
l=[mash[i] for i in range(len(mash)) if i%2==0]
l1=[mash[i] for i in range(len(mash)) if i%2!=0]
for j in range(len(mash)//2):
  print(l1[j]+l[j],end="")
