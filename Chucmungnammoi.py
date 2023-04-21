

l=[]
dem = 0
n = int(input())
for i in range(n):
    x = input()
    if x not in l:
        l.append(x)
        dem += 1
print(dem)