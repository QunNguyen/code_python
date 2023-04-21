
import math


def tinhtoan(a,b):
    return (a//math.gcd(a,b),b//math.gcd(a,b))
    
a,b=map(int,input().split())
res=tinhtoan(a,b)

print(res[0],end='')
print('/',end='')
print(res[1],end='')