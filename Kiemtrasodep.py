

def check(a):
    for i in range(0,len(s),2):
       for i in range(2, len(a), 2):
        if (a[i] != a[0]): return False
    for i in range(3, len(a), 2):
        if (a[i] != a[1]): return False
    return True


n=int(input())

for i in range(n):
    s=input()
    if check(s) :print("YES")
    else :print("NO")
    