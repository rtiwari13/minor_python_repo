class Student:
 def __init__(self,name,roll):
  self.name=name
  self.roll=roll
  print("Parameterized Contructor invoked")
 def display(self):
  print("Student roll number is" , self.roll)
  print("Student name is ",self.name)
obj = Student("Mobzilla Ronald",101)
obj1 = Student("pablo Picaso",103)
obj.display()
obj1.display()
    