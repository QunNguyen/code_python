


import re
N = int(input())
for i in range(N):
    l = list(int(x) for x in re.findall('\d+',input()))
    print(sorted(l)[0])