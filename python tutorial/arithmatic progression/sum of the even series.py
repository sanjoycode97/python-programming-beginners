#sum of the even number of series and their sum 1 to n
#n is your limit you want to print
sum=0
n=int(input("enter limit you want the even number: "))
for x in range(2,n+1,2):
    print(x)
    sum=sum+x
print()
print("sum of even number",sum)