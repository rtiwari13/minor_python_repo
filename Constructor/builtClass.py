class Employee:
  def __init__(self,name,id,age):
   self.name=name
   self.id = id
   self.age=age
  def display(self):
   print("Employee name is ",self.name)
   print("Employee id is ",self.id)
   print("Employee age is ",self.age)
emp = Employee("Ronald",101,23)
emp.display()
print(emp.age)
print(getattr(emp,'name'))
setattr(emp,'name',"Abc")
print(getattr(emp,'name'))
delattr(emp,'age')
print(hasattr(emp,'id'))
print(emp.__dict__)
print(emp.__module__)
print(emp.__doc__)