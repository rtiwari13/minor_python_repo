class A:
    a=None
    b=None
    def disp(self):
     print("Value of a",self.a) 
     print("Value of b",self.b)  
class B:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def disp(self):
        print(self.a+self.b)
obj = B(4,8)
obj.disp()
obj1=A()
obj1.disp()

     