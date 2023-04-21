

import math


def tong(s):
    tong=0
    for i in range(len(s)):
        tong+=int(s[i])
    return tong
        
def check(n):
    if(n<2): return False 
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
        
n=int(input())
for i in range(n):
    s=input()
    if check(tong(s)): print("YES")
    else :print("NO")
    