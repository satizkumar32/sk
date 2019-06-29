numb=input()
xxx=0
for i in range(len(numb)):
  if(numb[i].isdigit() or numb[i].isalpha() or numb[i]==(' ')):
    continue
  else:
    xxx+=1
print(xxx)
