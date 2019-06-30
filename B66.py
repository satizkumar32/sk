ns =int(input())
if(ns>1):
   for i in range(2,ns):
       if (ns % i) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
