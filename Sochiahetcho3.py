
def check(n):
    tong =0
    for i in range(n):
        tong+=int(s[i])
    return tong

n=int(input())
for i in range(n):
    s=input()
    if (check(s)%3==0): print("YES")
    else :print("NO")