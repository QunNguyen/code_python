
import math


def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True

t=int(input())
for i in range(t):
    n=int(input())
    dem=0
    for i in range(2,n):
        if(i+6)>n or (i+2)>n or (i+4)>n : break
        if snt(i) and (snt(i+2)or snt(i+4)) and snt(i+6): 
            dem+=1
            # print(i)
    print(dem)