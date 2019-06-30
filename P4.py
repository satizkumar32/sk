numb1,numb2=input().split()
r=0
if len(numb1)>len(numb2):
 numb1,numb2=numb2,numb1
p=0
while p<len(numb1):
 r+=(ord(numb2[p])-ord(numb1[p]))
 p+=1
for p in range(p,len(numb2)):
 r+=ord(numb2[p])-ord('a')+1
print(r)
