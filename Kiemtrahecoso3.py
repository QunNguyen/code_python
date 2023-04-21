
def check(s):
    for i in range(len(s)):
        if(s[i]!='1' and s[i]!='2'and s[i]!='0'):
            return False
    return True


n=int(input())
for i in range(n):
    s=input()
    if check(s):
        print("YES")
    else :print("NO")            