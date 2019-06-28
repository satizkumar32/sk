mass,mash=map(str,input().split())
if(len(mass)!=len(mass)):
  print("no")
c=[mass.count(i) for i in mass]
d=[mash.count(i) for i in mash]
if c==d:
  print("yes")
else:
  print("no")
