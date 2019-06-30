ds,f=list(map(int,input().split()))
w=ds*f
for x in range(0,w+1):
  if(x**2==0):
    print("yes")
    break;
else:
  print("no")
