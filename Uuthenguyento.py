


import math


def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):return False
    return True

def check(n):
    if (snt(len(n))==False): return False
    sum_snt=0
    sunm_notsnt=0
    for i in range(len(n)):
        if snt(int(n[i])):
            sum_snt+=1
        else: sunm_notsnt+=1
    if(sum_snt<sunm_notsnt): return False
    return True
    

T = int(input())
for t in range(T):
    a = input()
    if check(a):
        print("YES")
    else :print("NO")
