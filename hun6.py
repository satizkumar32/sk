aa=int(input())
bb=input()
cc=''
for i in bb:
    if i in cc and i!=" ":
        print(int(i))
        break
    else:
        cc+=i
if cc==bb:
    print("unique")
