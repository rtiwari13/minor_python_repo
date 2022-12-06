try:
 file_var=open(r"C:\Users\Asus\Desktop\pyfolder\ind.txt","r")
 print(file_var.readline())
except:
 print("file not found create it first")
     