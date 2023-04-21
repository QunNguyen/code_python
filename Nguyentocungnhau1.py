
def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

n=int(input())
a=list(int(x) for x in input().split())
a.sort()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(gcd(a[i],a[j])==1):
            print(a[i],a[j],end='')
            print()
            