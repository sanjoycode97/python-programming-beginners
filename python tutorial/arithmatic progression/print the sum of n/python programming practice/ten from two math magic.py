t=int(input("enter the number for test cases: "))
while t!=0:
    n=int(input("enter the number: "))
    if n%10==0:
        print(0)
    elif n%5==0:
        print(1)
    else:
        print(-1)
    t=t-1