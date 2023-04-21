

from re import T


def check(s):
    if(len(s)%2==0): return False
    for i in range(0,len(s)-2,2):
        if(s[i]!=s[i+2]): return False
    if(s[i]==s[i+1]): return False
    return True

n=int(input())
for i in range(n):
    s=input()
    if check(s): print("YES")
    else :print("NO")