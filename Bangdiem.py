
class hs:
    def __init__(self,ma,ten):
      self.ten=ten
      self.ma="HS"+str(format(ma,"02d"))
      self.diem=0
      self.hocluc=""
      
    def xeploai(self):
        if(self.diem<5): self.hocluc="YEU"
        if(5<= self.diem and self.diem<=6.9): self.hocluc="TB"
        if(7<= self.diem and self.diem<=7.9): self.hocluc="KHA"
        if(8<= self.diem and self.diem<=8.9): self.hocluc="GIOI"
        if(9<=self.diem): self.hocluc="XUAT SAC"
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(format(round(self.diem,2),".1f"))+' '+str(self.hocluc)

t=int(input())
a=list()
for i in range(1,t+1):
    name=input()
    std=hs(i,name)
    b=input().split()
    tong=0
    for j in range(len(b)):
        if(j<2):tong+=float(b[j])*2
        else :tong+=float(b[j])
    std.diem=float(round(float(tong/12),2))
    std.xeploai()
    a.append(std)
    
def xep(a):
    return a.diem

def xep1(a):
    return a.ma

a.sort(key=xep1,reverse=False)
a.sort(key=xep,reverse=True)

for i in a:
    print(i)
    
