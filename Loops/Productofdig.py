num =int(input("Enter  number"))
mul =1
while num>1 :
    rem = num%10
    mul = mul*rem
    num = num//10
print("Product of digit is ",mul)