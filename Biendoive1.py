from pickle import TRUE


while TRUE:
    a=[]
    n=int(input())
    if(n==0):
        break
    if(n==1):
        print(1)
        continue
    tmp=n
    while(tmp!=1):
        if(tmp%2==0):
            tmp=int(tmp/2)
            
        else:
            tmp=tmp*3+1
        if(tmp not in a):
            a.append(tmp)
    print(len(a)+1)