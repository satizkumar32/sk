jk=int(input())
jk=str(jk)
f=0
for i in range(0,len(jk)):
 if(jk[i]=='0' or jk[i]=='1'):
  f=1
 else:
  f=0
  break
if(f==1):
 print('yes')
else:
 print('no')
