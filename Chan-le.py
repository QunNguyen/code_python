
from doctest import FAIL_FAST
from itertools import count
from pickle import TRUE
import re


def check(s):
    count=0
    for i in range(len(s)):
        count+=int(s[i])
    if(count%10 != 0): return False
    for i in range(len(s)-1):
        if(abs(int(s[i])-int(s[i+1])) != 2):
            return False
    return TRUE
        

n=int(input())
for i in range(n):
    s=input()
    if check(s):print("YES")
    else :print("NO")