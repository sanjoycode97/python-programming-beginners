num1=int(input("enter the number 1 :"))
num2=int(input("enter the number 2 :"))
def sumdisplay(num1,num2):
    def sumfunc(num1,num2):
        return num1+num2
    return sumfunc(num1,num2)
total=sumdisplay(num1,num2)
print(total)
print(sumdisplay(num1,total))#eta sum jeta return korbe displaysum function
# tar saathe 1st number er sum korte korte thkbe

