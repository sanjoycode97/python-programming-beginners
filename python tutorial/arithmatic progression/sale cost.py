t=float(input())
while(t!=0):
    c=float(input())
    q=float(input())
    if q<=100:
        print(q*c)
    else:
        print(q*c-q*c*20/100)
    t=t-1

