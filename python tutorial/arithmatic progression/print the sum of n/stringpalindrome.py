str=input("enter the string: ")
str=str.casefold()
if str==str[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")