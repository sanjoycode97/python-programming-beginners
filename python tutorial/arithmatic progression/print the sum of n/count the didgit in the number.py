num=int(input("enter the number: "))
count=0
while num!=0:
    num=int(num/10)
    count=count+1
print(count)