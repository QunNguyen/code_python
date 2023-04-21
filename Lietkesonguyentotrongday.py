
import math


def snt(x):
    if(x<2): return 0
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return 0
    return 1

n=int(input())
a=list(int(x)for x in input().split())
b=[]
for i in(range(len(a))):
    if(snt(a[i])):
        if(a[i] not in b) :
            b.append(a[i])
            print(a[i],a.count(b[len(b)-1]),end=' ')
            print()
# print(b)