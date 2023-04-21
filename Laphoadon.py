class hoadon:
    def __init__(self, ma, ten):
      self.ma="KH"+ str(format(ma,'02d'))
      self.ten=ten
      self.tien=0
    def tinhtien (self,csm, csc):
        tmp=csc-csm
        if(0<=tmp and tmp<=50): 
            self.tien=tmp*100*1.02
        if(51<=tmp and tmp<=100): 
            self.tien=(50*100+(tmp-50)*150)*1.03
        if(tmp>100): 
            self.tien=(50*100+50*150+(tmp-100)*200)*1.05
            
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(round(self.tien))
t=int(input())
a=list()
for i in range(1,t+1):
    std=hoadon(i,input())
    std.tinhtien(int(input()),int(input()))
    a.append(std)
    
def xep(a):
    return a.tien
a.sort(key=xep,reverse=True)
for i in a:
    print(i)