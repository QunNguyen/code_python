

class luongmua:
    def __init__(self,ma,ten, bd,kt,luongmua):
      self.ma="T"+str(format(ma,"02d"))
      self.ten=ten
      self.bd=bd
      self.kt=kt
      self.luongmua=int(luongmua)
      self.thoigianmua=0
      self.thoigian()
      
    def thoigian(self):
        time1=int(self.bd[:-3])*60+int(self.bd[3:])
        time2=int(self.kt[:-3])*60+int(self.kt[3:])
        self.thoigianmua=time2-time1
        
    def tinhtoan(self):
        return round(self.luongmua*60/self.thoigianmua,2)
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(format(self.tinhtoan(),".2f"))
    
t=int(input())
a=list()
for i in range(1,t+1):
    std=luongmua(i,input(),input(),input(),input())
    tmp=False
    for j in a:
        if(std.ten==j.ten):
            j.luongmua+=std.luongmua
            j.thoigianmua+=std.thoigianmua
            tmp=True
            break
    if(tmp==False):
        a.append(std)
    else : tmp=False
                      
for i in a:
    i.tinhtoan()
    print(i)