
class chuyencan:
    def __init__(self,ma,ten,lop):
      self.ma=ma
      self.ten=ten
      self.lop=lop
      self.diem=10
      self.ghichu=""
    def tinhdiem(self,diemdanh):
        for i in diemdanh:
            if(i=="m"): self.diem-=1
            if(i=="v"): self.diem-=2
        if(self.diem <=0): 
            self.ghichu+="KDDK"
            self.diem=0
        
    def __str__(self) -> str:
       return self.ma+' '+self.ten+' '+self.ten+' '+str(self.diem)+' '+self.ghichu
t=int(input())
a=list()

for i in range(1,t+1):
    std=chuyencan(input(),input(),input())
    a.append(std)
    
for i in range(1,t+1):
    b,c=input().split()
    for j in a:
        if(b==j.ma):
            j.tinhdiem(c)
for i in a:
    print(i)