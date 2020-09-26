from math import *
#1+x+x2/2!+x3/3!+x4/4!+......10 terms
sum=0
p=0
x=2
for i in range(0,10):
    print(pow(x,p)/factorial(i))
    sum=sum+pow(x,p/factorial(i))
    p=p+1
print(sum)
