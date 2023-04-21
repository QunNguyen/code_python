
from pickle import TRUE


n=int(input())
for i in range(n):
    s=input()
    check =True
    for i in range(len(s)-1):
        if(s[i]>s[i+1]):
            check=False
    if check : print ("YES")
    else :print("NO")
