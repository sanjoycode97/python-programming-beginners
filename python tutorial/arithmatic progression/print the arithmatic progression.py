#a=first term of the series the common d=difference is 5 and we will print the series upto 10th term
#2,7,12,17,22.....upto 10th term,a=a+d
a=int(input("enter the first term you want : "))
d=int(input("enter the  common differ you want : "))
n=int(input("enter the limit upto : "))
for x in range(0,n+1):
    print(a)
    a=a+d