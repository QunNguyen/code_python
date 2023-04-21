
s=input()
k=0

for i in range(0,len(s)):
    if(int(s[i])==7 or int(s[i])==4): k+=1

if(int(k)==4 or int(k)==7):print("YES")
else: print("NO")