n = int(input("enter a number"))
temp=n
sum=0
while n>0 :
    dig = n%10
    sum= sum+(dig*dig*dig)
    n = n//10
if temp==sum : print("armstrong number")
else : print("not an armstrong number")