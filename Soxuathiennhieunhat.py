t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x)for x in input().split()]
    b={}
    for i in a:
        if(i in b):
            b[i]=b[i]+1
        else:
            b[i]=1
    maxx = 0
    res = 0
    for key, val in b.items():
        if val > maxx:
            maxx = val
            res = key
    # print(int(N/2))
    if (maxx > int(n/2)):
        print(res)
    else:
        print('NO')