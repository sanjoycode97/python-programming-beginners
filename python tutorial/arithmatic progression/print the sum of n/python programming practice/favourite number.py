t=int(input("enter the test case: "))
while t!=0:
 n=int(input("enter the number: "))
 count=0
 temp=n
 while temp!=0:
    r=temp%10
    if r==5:
        count=count+1
    temp=int(temp/10)
 print(count)
 t=t-1
