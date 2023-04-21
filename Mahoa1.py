
from itertools import count
from tkinter import END


n=int(input())

for i in range(n):
    s=input()
    count={}
    for i in s:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
for i in range(count.get()):
    print(s[i], count[i])