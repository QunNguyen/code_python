
def check (x, y):
    return len(str(x))>len(str(y))
    

t=int(input())
for i in range(t):
    n=int(input())
    a=list(int(x)for x in input().split())
    a.sort(0,len(a)-1,key=check)
    print(a)
    