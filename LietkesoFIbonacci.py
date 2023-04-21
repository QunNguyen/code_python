
def fibo(n):
    f1 = 1
    f2 = 1
    fn = 1
 
   
    if (n == 1 or n == 2):
        return 1
    else:
        for i in range(2, n):
            f2 = f1
            f1 = fn
            fn = f2 + f1
        return fn


n=int(input())
for i in range(n):   
    [a,b]=list(int(i) for i in input().split())
    for i in range(a,b+1):
        print(fibo(i),end=' ')
    print()