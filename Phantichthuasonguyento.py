
from itertools import count
import math


n=int(input())
for i in range(n):
    n=int(input())
    print("1",end='')
    for i in range(2,int(math.sqrt(n))+1):
        count=0
        while(n%i==0):
            count+=1
            n/=i
        if(count>0): print(" * "+str(i)+"^"+str(count),end='')
    if(n>1):
        print(" * "+str((int(n)))+"^1",end='')
    print()