class A:
 a=None
 b=None
 def disp(self):
  print("value of a ",self.a)
  print("value of b",self.b)
class B :
 def add(self):
  print("Addition is " ,self.a+self.b)
class C(A,B):
 def __init__(self,x,y):
  self.a=x
  self.b=y
 def mul(self):
   print("Multiplication",self.a*self.b)
a=int(input("Enter your number"))
b=int(input("Enter your second number"))
obj = C(a,b)
obj.disp()
obj.add()
obj.mul()
print(issubclass(C,A))
print(issubclass(C,B))
print(issubclass(B,A))