n,q=map(int,input().spli())
if(q<=100000):
    for x in range(n+1,q):
        if(x%2!=0):
          print(x,end=" ")
