num=int(input("enter the number: "))
pow=int(input("enter the pow: "))
sum=1
for x in range(pow):
    sum=sum*num
print("power of given number is : ",sum)
sum=1
i=1
while i<=pow:
    sum=sum*num
    i=i+1
print(sum)