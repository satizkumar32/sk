from collections import Counter
xxx = int(input())
yyy = list(map(int,input().split()))
zzz = Counter(yyy)
list = []
for i in zzz.items():
  if(i[1] != 1):
    print(i[0],end = " ")
for j in zzz.items():
  list.append(j[1])
if(max(list) == 1):
  print("unique")
