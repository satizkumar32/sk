ee=int(input())
dd=list(map(int,input().split()))
for aa in range(0,ee-2):
    for bb in range(aa+1,ee-1):
        for cc in range(bb+1,ee):
            if(dd[aa]+dd[bb]==dd[cc]):
                print(dd[aa], dd[bb], dd[cc]
