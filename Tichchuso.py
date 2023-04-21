
def check(s):
    tich=1
    for i in range(len(s)):
        if(s[i]!='0'): tich*=int(s[i])
    return tich
        

n=int(input())
for i in range(n):
    s=input()
    print(check(s))