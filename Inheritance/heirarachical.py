class A:
 a=None
 b=None
 def disp(self):
  print("value of a ",self.a)
  print("value of b",self.b)
class B(A) :
 def __init__(self,x,y):
     self.a=x
     self.b=y
 def add(self):
  print("Addition is " ,self.a+self.b)
class C(A):
 def __init__(self,x,y):
  self.a=x
  self.b=y
 def mul(self):
   print("Multiplication",self.a*self.b)
a=int(input("Enter your number"))
b=int(input("Enter your second number"))
obj1 = B(a,b)
obj2=C(a,b)
obj1.disp()
obj1.add()
obj2.mul()