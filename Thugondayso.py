


from operator import le
from textwrap import indent


n=int(input())
arr = list(int(i) for i in input().split())

i=0
while(i<len(arr)-1):
    if((arr[i]+arr[i+1])%2==0):
        del(arr[i])
        del(arr[i])
        # print(arr)
        if(i>0) :i=i-1
    else :i+=1
print(len(arr))