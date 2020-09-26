
a=[]
n=int(input("enter the range: "))
for values in range(n):
    element=int((input("enter the elements: ")))
    a.append(element)

b=[]
for values in a:
    if values not in b:
        b.append(values)
print(b)