a=0
b=1
n=int(input("enter the limit upto want fibo: "))
print(a," ",b)
for x in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c
