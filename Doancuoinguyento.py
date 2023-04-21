



import math


def tong(s):
    a=""
    for i in range(len(s)-4,len(s),1):
        a+=str(s[i])
    if check(int(a)) :return True
    else :return False
        
def check(n):
    if(n<2): return False 
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
        
n=int(input())
for i in range(n):
    s=input()
    if tong(s): print("YES")
    else :print("NO")
    