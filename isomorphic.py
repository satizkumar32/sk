as,ast=map(str,input().split())
if(len(as)!=len(as)):
  print("no")
c=[as.count(i) for i in as]
d=[ast.count(i) for i in ast]
if c==d:
  print("yes")
else:
  print("no")
