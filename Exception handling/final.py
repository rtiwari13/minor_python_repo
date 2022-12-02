a=10
b=10
try:
 c=a/(a-b)
 print(c)    
except:
 c=a/(a-b)  
 print("zero division error") 
finally:
 print("finally bolck executed")      