

n=int(input())
a=[]
for i in range(n):
    b=list(int(x) for x in input().split())
    a.append(b)  
k=int(input())
# print(a)
tong1=0
tong2=0
for i in range(n):
    for j in range(n):
        if(i<j):
            tong1+=a[i][j]
        if(i>j): 
            tong2+=a[i][j]
if(abs(tong1-tong2)<k):
    print("YES")
else :print("NO")
print(abs(tong1-tong2))