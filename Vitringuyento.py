

import math

def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True

def check(s):
    for i in range(len(s)):
        if snt(i):
            if(s[i]!='2'and s[i]!='3'and s[i]!='7' and s[i]!='5'):
                return False
        else:
            if(s[i]=='2'or s[i]=='3'or s[i]=='7' or s[i]=='5'):
                return False
    return True

n=int(input())
for i in range(n):
    s=input()
    if check(s): print("YES")
    else :print("NO")