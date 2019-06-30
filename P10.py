aaa=int(input())
bbb=[int(i) for i in input().split()]
xxx=0
for i in range(aaa):
   for j in range(i):
      if bbb[j]<bbb[i]:
         xxx+=bbb[j]
print(xxx)
