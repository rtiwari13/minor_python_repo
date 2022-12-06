try:
 with open(r"C:\Users\Asus\Desktop\pyfolder\index.txt") as f1:
  with open(r"C:\Users\Asus\Desktop\pyfolder\index1.txt") as f2:
   for i in f1: 
    f2.write(i)
except:
 print("data copied successfully")
else :
 print("File does not exist create it first")    
