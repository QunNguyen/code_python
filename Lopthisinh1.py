from datetime import datetime


class thisinh:
    def __init__(self, ten, ngaysinh,diem1,diem2,diem3):
      self.ten=ten
      self.ngaysinh=ngaysinh
      self.diem1=diem1
      self.diem2=diem2
      self.diem3=diem3
    def tinhdiem(self):
        tong=float(self.diem1)+float(self.diem2)+float(self.diem3)
        return format(tong,".1f")
    
    def chuanhoangay(self):
        ngay=self.ngaysinh.split('/')
        return format(int(ngay[0]),"02d")+'/'+format(int(ngay[1]),"02d")+'/'+format(int(ngay[2]),"02d")
        
    def __str__(self) -> str:
        return self.ten+' '+str(self.chuanhoangay())+' '+self.tinhdiem()

tmp=thisinh(input(),input(),input(),input(),input())
print(tmp)
# dt = datetime.strftime(demo_str, "%d%m%Y")

    