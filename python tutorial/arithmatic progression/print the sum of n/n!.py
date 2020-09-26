#1+2/2!+3/3!+4/4!.....n/n!----factorial means if 3!=3*2*1
n=int(input("enter the range : "))
fact=1
sum=0
for x in range(1,n+1):
    fact=fact*x
    print(fact)
    sum=sum+x/fact
print("sum of number",sum)