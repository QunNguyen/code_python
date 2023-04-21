
def check(a,b):
    for j in range(n):
        if(a[j]>b[j]): return False
    return True

t=int(input())
for i in range(t):
    n=int(input())
    ar=list(int(i) for i in input().split())
    br=list(int(x) for x in input().split())
    ar.sort()
    br.sort()
    if (check(ar,br)):print("YES")
    else :print("NO")
    
     