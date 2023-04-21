

import math


def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

n=int(input())
for i in range(n):
    s=input()
    a=s[::-1]
    # print(s,a)
    if(gcd(int(a),int(s))):
        print("YES")
    else:print("NO")