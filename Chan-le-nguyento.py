

import math
from re import T, match
from trace import Trace


def check(s):
    for i in range(len(s)):
        if(i%2==0):
            if(int(s[i])%2!=0): return False
        else:
            if(int(s[i])%2==0): return False
    return True

def check1(s):
    tong=0
    for i in range(len(s)):
        tong+=int(s[i])
    if(snt(tong)==False) :return False
    return True

def snt(n):
    if(n<2): return False 
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True

n=int(input())
for i in range(n):
    s=input()
    if check(s)and check1(s): print("YES")
    else :print("NO")