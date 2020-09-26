m=int(input("enter the first interval: "))
n=int(input("enter the number of range you want: "))
for x in range(m,n+1):
    cn=x
    fact=1
    for y in range(1,cn+1):
        fact=fact*y
    print(cn,":",fact)