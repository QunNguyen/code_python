
n=int(input())

for i in range(n):
    s=input()
    if(s[0]!=s[len(s)-2] or s[1]!=s[len(s)-1]): print("NO")
    else: print("YES")