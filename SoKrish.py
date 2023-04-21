

def giaithua(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum

t=int(input())
for i in range(t):
    n=input()
    tong=0
    for i in range(len(n)):
        # print(giaithua(int(n[i])))
        tong+=giaithua(int(n[i]))
    if(tong==int(n)): print("YES")
    else :print("NO")
    