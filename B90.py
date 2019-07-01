sk=str(input())
l=[]
for i in sk:
    if (i.isnumeric()):
        l.append(i)
print(sep="",*l)
