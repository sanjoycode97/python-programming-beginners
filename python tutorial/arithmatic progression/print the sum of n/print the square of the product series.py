#1*1 X 2*2 X 3*3 X.....nXn
prod=1
for x in range(1,11):
    print(x*x)
    prod=prod*x*x
print("the product series is ",prod)