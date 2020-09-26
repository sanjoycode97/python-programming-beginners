n = int(input("enter the number: "))
def palindrome_func(n):
    def another(num):

     temp=num
     sum=0
     while temp!=0:
        r=int(temp%10)
        sum=sum*10+r
        temp=int(temp/10)
     if sum==num:
        return "pallindrome"
    return another(n)
palindrome=palindrome_func(n)
print(palindrome)
