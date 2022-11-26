num = int(input("enter a number"))
temp=num 
sum =0
while num>0:
    rem = num%10
    sum = sum*10+rem
    num = num//10
if temp==sum :
    print("Number is Pallindrome",sum)    
else :
    print("Not a pallindrome" ,sum)    