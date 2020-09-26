m=int(input("enter the first range: "))
n=int(input("enter the last range: "))
sum1=0
sum2=0
for x in range(m,n+1):
    if x%2==0:
        sum1=sum1+x
    else:
        sum2=sum2+x
print(" ",sum1)
print(" ",sum2)