from pickle import TRUE
from traceback import print_tb


def check(a):
    return a[0]==a[1] and a[2]==a[3] and a[1]==a[2]

while True:
    b=list(int(x)for x in input().split())
    if(check(b) and b[0]==0):
        break
    dem=0
    while check(b)==False:
        tmp=b[0]
        dem+=1
        b[0]=abs(b[0]-b[1])
        b[1]=abs(b[1]-b[2])
        b[2]=abs(b[2]-b[3])
        b[3]=abs(b[3]-tmp)
        # print(b)
    print(dem)
    