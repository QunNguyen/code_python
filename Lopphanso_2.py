
import math


class Phanso:
    def __init__(self, x, y):
      self.x = int(x)
      self.y=int(y)
    def tinhtoan(self ,p):
       tu=(self.x*p.y+p.x*self.y)
       mau=self.y*p.y
       print(tu//math.gcd(tu,mau),end='')
       print('/',end='')
       print(mau//math.gcd(tu,mau),end='')
a=input().split()
p=Phanso(a[0],a[1])
p1=Phanso(a[2],a[3])
p.tinhtoan(p1)
