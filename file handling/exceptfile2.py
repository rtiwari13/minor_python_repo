try:
 file_var=open(r"C:\Users\Asus\Desktop\pyfolder\index.txt","r")
 print(file_var.readline())
except:
 print("file not found create it first")
else:
 file_var.close()
 print("file closed successfully")