file_var=open(r"C:\Users\Asus\Desktop\pyfolder\index.txt","w")
file_var.write("This is minor november training of Python , File Handling in python. We created a file say text file and then wrote some text via file access methods ")
print("data is being written in index text fle")

file_var=open(r"C:\Users\Asus\Desktop\pyfolder\index.txt","r")
print(file_var.read(1000))
print(file_var.readline(1))
print(file_var.readline())