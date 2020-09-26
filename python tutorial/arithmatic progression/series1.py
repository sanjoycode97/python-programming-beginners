a=int(input("enter the first number= "))
n=int(input("enter the upto: "))
d=23
for x in range(0,n+1):
    print(a)#first print 147
    a=a-(d-x*2)#then 147-(23-0*2)=124 then print 124 then 124-(23-1*2)=103
