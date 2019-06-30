pq=int(input())
s=int(pq/2)
q=0
for i in range (2,s+1):
    if pq % i == 0:
        q=1
        print("yes")
        break
if q == 0:
    print("no")
