class rectangle:
    def __init__(self,length,breadth):
     self.length=length
     self.breadth=breadth

    def area(self):
        print("the area is",self.length*self.breadth)
    def perimeter(self):
        print("the perimeter is",2*self.length+self.breadth)

r=rectangle(20,40)
print("length is",r.length)
print("breadth is",r.breadth)
r.area()
r.perimeter()
