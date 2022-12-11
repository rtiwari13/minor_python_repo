class Parent:
 def dis(self):
     print("Normal method derived clss")
class Child(Parent):
    def display(self):
        print("base class")
obj = Child()
obj.dis()
obj.display()