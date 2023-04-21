
import math


def snt(n):
    if(n<2):return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):return False
    return True

def check(s):
    tong=0
    for i in range(len(s)):
        if(snt(int(s[i]))==False): return False
        tong+=int(s[i])
    if(snt(tong)==False): return False
    return True

t=int(input())
for i in range(t):
    s=input()
    if snt(int(s)) and snt(int(s[::-1])) and check(s) : print("Yes")
    else :print("No")
