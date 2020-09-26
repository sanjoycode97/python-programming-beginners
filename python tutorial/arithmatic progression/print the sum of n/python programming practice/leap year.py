year=int(input("enter the year: "))
print(year)
if year%400==0:
    print("the year is leap year")
elif year%100==0:
    print("the year is not the leap year")
elif year%4==0:
    print("the year is the leap year")
else:
    print("the year is not the leap year")