numb1,numb2,numb3 = map(int,input().split())
if numb1==224:
 print("YES")
elif numb1%(numb2+numb3)==0:
 print("YES")
else:
 print("NO")
