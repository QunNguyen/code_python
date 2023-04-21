

def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def mu(a):
    tong=10
    for i in range(1,a):
        tong*=10
    return tong

a,b=input().split()
tong=0
for i in range(mu(int(b)-1),mu((int(b)))):
    if(gcd(int(a),i)==1):
        tong+=1
        print(i,end=' ')
    if(tong==10):
        print()
        tong=0
