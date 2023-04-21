

from re import T


n=int(input())
for i in range(n):
    s=input()
    a=s[::-1]
    check =True
    for j in range(1,len(s)-1):
        if(abs(ord(s[j])-ord(s[j-1]))!=abs(ord(a[j])-ord(a[j-1]))):
            check =False
    if check:print("YES")
    else : print("NO")