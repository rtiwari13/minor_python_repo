import os
if os.path.exists(r"C:\Users\Asus\Desktop\pyfolder\file handling\index1.txt"):
 os.remove(r"C:\Users\Asus\Desktop\pyfolder\file handling\index1.txt")
 print("File removed successfully")
else:
 print("file not found") 