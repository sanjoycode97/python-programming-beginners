#*args and **kwargs
'''
def sum(*args):
    print(*args)
    sum=0
    for x in args:
        sum= sum+x
    print(sum)
add=sum(1,2,3,4,5)
print(add)
'''
#rules params,*args,default params,**kwargs
def super_func(*args,**kwargs):
    print(args)
    print(kwargs)
    total=0
    for x in kwargs.values():
        total=total+x
    return sum(args)+total
print(super_func(1,2,3,4,5,num1=5,num2=10))




















