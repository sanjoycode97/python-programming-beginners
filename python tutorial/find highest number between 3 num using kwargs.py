#this one is wrong method
def higest_number(**kwargs):
    num1=0
    num2=0
    num3=0
    for x in kwargs.values():
        if x>num1 and x>num2:
            return "highest n1"
        elif x>num2 and x>num3:
            return "higest is n2"
        return "higest is n3"
print(higest_number(num1=2,num2=3,num3=4))