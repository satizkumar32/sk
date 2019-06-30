numb,numb1=input().split()
sk=abs(len(numb)-len(numb1))
for i in range(len(numb)):
  if len(numb1)==1 and numb1[i] in numb:
   break
  if numb[i]!=numb1[i]:
   sk+=1
print(sk)
