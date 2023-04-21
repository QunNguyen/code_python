
n=int(input())
for i in range(n):
    s=input()
    for i in range(1,len(s),2):
        print(s[i-1]*int(s[i]),end='')
    print()