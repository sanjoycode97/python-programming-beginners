num=int(input("enter the number: "))
temp=num
sum=0
while temp!=0:
    r=temp%10
    sum=sum+r*r*r
    temp=int(temp/10)
if sum==num:
    print("number is armstrong")
else:
    print("number is not armstrong")