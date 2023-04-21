

def check(s,n):
    return s.find(n)

T = int(input())
for t in range(T):
    a=input()
    s=input()
    x=a.replace(s,"*")
    dem=0
    for i in range(len(x)):
        if(x[i]=='*'):
            dem+=1
    print(dem)