import math
ls=[int(i) for i in input().split()]
print(int(((ls[0]*ls[1])/(math.gcd(ls[0],ls[1])))))
