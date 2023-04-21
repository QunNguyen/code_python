


from datetime import datetime
import math
from pickle import TRUE


class  thoigian:
    def __init__(self, ma, ten):
      self.ma=ma
      self.ten=ten
      self.tong=0
    def tinhgio(self,bd,kt):
        gio=int(kt[:-3])-int(bd[:-3])
        phut=int(kt[3:])-int(bd[3:])
        if(phut<0):
            gio-=1
            phut+=60
        self.tong=gio*60+phut
        self.gio=str(gio)+' gio '+str(phut)+' phut'
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(self.gio)
        
t=int(input())
a=list()
for i in range(1,t+1):
    std=thoigian(input(),input())
    std.tinhgio(input(),input())
    a.append(std)
def xep(a):
    return a.tong
a.sort(key=xep,reverse=True)
for i in a:
    print(i)