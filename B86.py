ks=list(input())
p=[]
for i in ks:
   if i not in p:
      p.append(i)
if ks==p:
   print("Yes")
else:
   print("No")
