n=int(input("enter the limit you want: "))
sum=0
for x in range(1,n+1,2):
    print(x,end=" ")
    sum=sum+x
print()
print(sum,end=" ")
