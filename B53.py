numb=int(input())
sk=0
i=0
while numb > 0:
  i=num%10
  numb=numb//10
  sk=sk+i
print(sk)
