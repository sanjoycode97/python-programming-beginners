a=1
b=2
sign=1
n=int(input("enter the term: "))
l1=[]
print(a)
print(b)
for i in range(3,n+1):
    c=b- sign*a
    print(c)
    l1.append(c)

    a=b
    b=c
    sign=sign* -1
print("nth term is: ",l1[n-3])