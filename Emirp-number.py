
import math
from re import L


def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):return False
    return True

def check(s):
    if(s==s[::-1]): return False
    if snt(int(s))and snt(int(s[::-1])): return True
    return False

t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        if(check(str(i)) and int(str(i)[::-1])<n):
            if(i not in a) and (int(str(i)[::-1]) not in a):
                a.append(i)
                a.append(int(str(i)[::-1]))
    for a in a:
        print(a,end=' ')
    print()