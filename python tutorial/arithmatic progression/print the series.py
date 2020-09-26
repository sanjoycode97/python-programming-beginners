#1+1/2+1/3+.....+1/n
n=int(input("enter the number: "))
sum=0
for x in range(1,n+1):
    a= 1/x
    print(a)
    sum=sum+a
print("sum of the number is : ",sum)



