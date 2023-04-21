




import re


def checkNT(j):
    return j==j[::-1]

def check(a):
    if(len(a)%2==1): return False
    for i in range (len(a)):
        if(int(a[i])%2!=0): return False
    return True


n= int(input())
for i in range(n):
    a=int(input())
    for j in range(22,a):
        if(checkNT(str(j))and check(str(j))) :print(j,end=' ')
    print()    
