num1=int(input("enter the first age: "))
num2=int(input("enter the secnd age: "))
num3=int(input("enter the third age: "))

def find_oldest_man(num1,num2,num3):
    def ageidentity(n1,n2,n3):
        if n1>n2 and n1>n3:
            return("the oldest person is first person: ")
        elif n2>n1 and n2>n3:
            return ("the oldest person is second person: ")
        else:
            return("the oldest person is third person: ")
    return ageidentity(num1,num2,num3)
age=find_oldest_man(num1,num2,num3)
print(age)
