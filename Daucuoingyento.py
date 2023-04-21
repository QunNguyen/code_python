

import math


def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):return False
    return True
        

T = int(input())
for t in range(T):
    a = input()
    if snt(int(a[0:3])) and snt(int(a[len(a)-3:len(a)])):
        print("YES")
    else :print("NO")
    # print(a[0:2],a[len(a)-3:len(a)-1])
