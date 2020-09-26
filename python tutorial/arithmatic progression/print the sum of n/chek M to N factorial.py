m=int(input("enter the first number= "))
n=int(input("enter the second number= "))
fact=1
for i in range(m,n+1):
    for j in range(1,i+1):
        fact=fact*j
    print("the factorial is = ",fact)
    fact=1