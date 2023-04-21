n=int(input())
a=list(int(x)for x in input().split())
dem=0
for i in range(len(a)-1):
    if(a[i]!=a[i+1]):
        dem+=1
print(dem)