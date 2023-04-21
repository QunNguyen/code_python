
import math


class Phanso:
    def __init__(self, x, y):
      self.x = int(x)
      self.y=int(y)
    def tinhtoan(self):
        print(str(self.x//math.gcd(self.x,self.y))+'/'+str(self.y//math.gcd(self.x,self.y)))

a=input().split()
p=Phanso(a[0],a[1])
# print(p.x, p.y)
p.tinhtoan()
