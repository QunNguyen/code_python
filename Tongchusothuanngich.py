
def tong(s):
    tong=0
    for i in range(len(s)):
        tong+=int(s[i])
    return tong
        
def check(n):
    s=str(n)
    if(s==s[::-1]) : return True
    else :return False   

n=int(input())
for i in range(n):
    s=input()
    if check(tong(s)): print("YES")
    else :print("NO")
    