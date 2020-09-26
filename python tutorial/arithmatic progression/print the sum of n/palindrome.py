num=int(input("enter the number"))
temp=num
sum=0
while temp!=0:
    r=temp%10
    sum=sum*10+r
    temp=int(temp/10)
if sum==num:
    print("palindrome")
else:
    print("not palindrome")