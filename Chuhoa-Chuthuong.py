
s=input()
dem=0
for i in range(len(s)):
    if('a'<=s[i] and s[i]<='z'):
        dem+=1
    else: dem-=1

if(dem<0): print(s.upper())
else : print(s.lower())