n=int(input("enter the number: "))
count=0
for x in range(1,n+1):
    if n%x==0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("not prime")