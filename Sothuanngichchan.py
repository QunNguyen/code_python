
from cgi import print_form


def check(s):
    if(len(s)%2!=0) : return False
    if(s!=s[::-1]): return False
    for i in range(len(s)):
        if(int(s[i])%2!=0):
            return False
    return True

n=int(input())
for i in range(n):
    s=int(input())
    for i in range(21,s):
        if(check(str(i)) and int(str(i)[0])%2==0):
            print(i,end=' ')
    print()
    