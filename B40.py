numb=int(input())
fiboon,gas=0,1
print(gas,end=" ")
for i in range(1,numb):
  yyy=fiboon+gas
  print(yyy,end=" ")
  fiboon,gas=gas,yyy
