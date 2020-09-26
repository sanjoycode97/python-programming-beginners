m=int(input("enter the first number: "))
n=int(input("enter the second number: "))
count=0
for x in range(m,n+1):
    for y in range(1,x+1):
        if x%y==0:
            count=count+1
    if count==2:
        print("prime numbers are= ",x)

    count=0