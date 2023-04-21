from pickle import TRUE



def check(s):
    for i in range(len(s)):
        if(int(s[i])!=7 and int(s[i])!=4 ): return False
    return TRUE
        
n =int(input())
for i in range(n):
    s=input()
    if check(s): print("YES")
    else : print("NO")