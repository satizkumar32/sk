sk=str(input())
kk=0
ll=0
mm=len(sk)
for i in range(0,mm):
  if sk[i].isalpha():
    kk=kk+1
  if sk[i].isnumeric():
    ll=ll+1
if kk == 0 or ll == 0:
  print("No")
else:
  print("Yes")
