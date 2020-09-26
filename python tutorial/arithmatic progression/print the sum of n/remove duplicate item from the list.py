a=[]
n=int(input("enter the number of range of the list: "))
for x in range(1,n+1):
    element=int(input("enter the element of list: "))
    a.append(element)
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)
