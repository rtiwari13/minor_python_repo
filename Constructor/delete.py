class orient:
 roll =101
 name = "Mobzilla Ronald"
 def display(self):
  print("Student roll number is",self.roll)
  print("Student name is",self.name)
  print(self.roll)
obj = orient()
obj.display()
del obj.display
del obj.name
