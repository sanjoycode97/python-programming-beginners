date=input("enter the date: ")
month=input("enter the month: ")
year=input("enter the year: ")
givendate=date+month+year
if givendate==givendate[::-1]:
    print("palindrome")
else:
    print("not pallindrome")