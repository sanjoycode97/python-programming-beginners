#print the product series=1*2*3*4*5...n
n=int(input("enter the range you want: "))
prod=1

for x in range(1,n+1):
    print(x)
    prod=prod*x


print("sum of their product= ",prod)