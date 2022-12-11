class A:
    a=10
    _b=20
    __c=None
    print(a,"\n",_b,"\n",__c)
    def disp(self):
     print(self.a)
     print(self._b)
     self.__c=self.a+self._b
obj = A()
obj.disp()
print(obj.a)
print(obj._b)
print(obj.__c)

     