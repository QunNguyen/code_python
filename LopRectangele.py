
class Rectangle:
    def __init__(self, x, y, color):
      self.x=x
      self.y=y
      self.z=color
    def perimeter(self):
        return (self.x+self.y)*2
    def area(self):
        return (self.x*self.y)
    def color(self):
        return self.z.title()
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print(r.perimeter(), r.area(), r.color())
        t -= 1