class nhanvien:
    def __init__(self,ma,ten,diemlythuyet,diemthuchanh):
      self.ma="TS"+format(ma,"02d")
      self.ten=ten
      self.diemlythuyet=str(diemlythuyet)
      self.diemthuchanh=str(diemthuchanh)
      self.ghichu=""
      self.diem=0
      self.chuanhoa()
    def chuanhoa(self):
        if(float(self.diemlythuyet)>10):
           if(len(self.diemlythuyet)<3): self.diemlythuyet=float(self.diemlythuyet[0])+float(self.diemlythuyet[1])*0.1
           else: self.diemlythuyet=float(self.diemlythuyet[0])+float(self.diemlythuyet[1])*0.1+float(self.diemlythuyet[2])*0.01
        else: self.diemlythuyet=float(self.diemlythuyet)
            
        if(float(self.diemthuchanh)>10):
            if(len(self.diemthuchanh)<3): self.diemthuchanh=float(self.diemthuchanh[0])+float(self.diemthuchanh[1])*0.1
            else: self.diemthuchanh=float(self.diemthuchanh[0])+float(self.diemthuchanh[1])*0.1+float(self.diemthuchanh[2])*0.01
        else: self.diemthuchanh=float(self.diemthuchanh)
        tb=float((self.diemlythuyet+self.diemthuchanh)/2)
        self.diem=tb
        
    def tinh(self):
        tb=self.diem
        if(tb<5): self.ghichu="TRUOT"
        if(5<=tb and tb<8): self.ghichu="CAN NHAC"
        if(8<=tb and tb<=9.5): self.ghichu="DAT"
        if(9.5<tb): self.ghichu="XUAT SAC"
        return format(tb,".2f")
    
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(self.tinh())+' '+self.ghichu+' '+str(self.diemlythuyet)+' '+str(self.diemthuchanh)
    
t=int(input())
a=list()
for i in range(1,t+1):
    std=nhanvien(i,input(),input(),input())
    a.append(std)
    
def xep(a):
    return a.diem
a.sort(key=xep,reverse=True)

for i in a:
    print(i)