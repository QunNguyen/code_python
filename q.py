class mathang:
    # def __init__(self,ma,ten,nhomhang,giaban,soluong):
    #   self.ma=ma
    #   self.ten=ten
    #   self.nhomhang=nhomhang
    #   self.giaban=giaban
    #   self.soluong=soluong
    def nhap(self,ma,ten,nhomhang,giaban,soluong):
          self.ma=ma
          self.ten=ten
          self.nhomhang=nhomhang
          self.giaban=giaban
          self.soluong=soluong
    def __str__(self) -> str:
       return self.ma+' '+self.ten+' '+self.nhomhang+' '+self.giaban+' '+self.soluong

def yeucau():
    print("yeucau")
while True:
    