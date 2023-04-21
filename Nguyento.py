
from cmath import sqrt
from math import fabs
import math
import re

def gcd(a,b):
    while(a>0):
        if(a<b):
            a,b=b,a
        a=a%b
    return b

def check(n):
    if(n<2): return False
    else :
         for i in range(2,int(math.sqrt(n)+1)):
            if(n%i==0): return False
    return True
    

n =int(input())
for i in range(n):
    a=int(input())
    k=0
    for i in range(a):
        if gcd(i,a)==1:
            k+=1
    if check(k):print("YES")
    else: print("NO")
        
    