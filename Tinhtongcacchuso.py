


t=int(input())
for i in range(t):
    tong=0
    s=input()
    x=list()
    for j in range(len(s)):
        if('0'<=s[j] and s[j]<='9'): tong+=int(s[j])
        else: x.append(s[j])
    x.sort()
    for k in x:
        print(k,end='')
    print(tong)