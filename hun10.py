mode,node=input().split()
kigs={int(kigs) for kigs in input().split()}
vigs={int(vigs) for vigs in input().split()}
if vigs.issubset(kigs):
    print("YES")
else:
    print("NO")
