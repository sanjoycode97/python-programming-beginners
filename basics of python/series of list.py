mylist=[]
e=0
m=0
mylist.append(e)
mylist.append(m)
n=int(input("enter the nth term: "))
for i in range(2,n+1):
    if i%2!=0:
        e=e+1
        mylist.append(e)
    else:
        m=m+2
        mylist.append(m)
print(mylist[n])