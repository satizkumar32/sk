ls=int(input())
b=[]
for i in range(0,ls):
    inpu=input()
    b.append(inpu)
li=[]
for i in zip(*b):
    if(i.count(i[0])==len(i)):
        li.append(i[0])
            
    else:
        break
print(''.join(li))
