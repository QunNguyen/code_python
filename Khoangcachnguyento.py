
import math


def snt(n):
    if(n<2):return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True


[a, b] = [int(x) for x in input().split()]

x=list()
dem=0
i=2
while(dem<a):
    if(snt(i)):
        x.append(i)
        dem+=1
    i+=1
    
tmp=b
j=0
print(tmp,end=' ')
while(j<a):
    tmp+=x[j]
    j+=1
    print(tmp,end=' ')
    dem+=1

