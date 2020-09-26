#print the series 1 6 16 31.....upto 10 term
a=int(input("enter the first element: "))
n=int(input("enter"))
d=int(input("enter the diff: "))

for x in range(0,n+1):

    a=a+x*d
    print(a)

