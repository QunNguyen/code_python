

from operator import truediv
from pickle import TRUE
from wsgiref.simple_server import demo_app


a=list()
test=10 
while test>0: 
    data=input() 
    base=data.split()
    a+=base
    test-=len(base)
r=list()
for i in a:
    so = int(i) % 42
    if (so in r) == False:
        r.append(so)
print(len(r))
