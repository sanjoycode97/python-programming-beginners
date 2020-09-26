a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
if a<b:
    hcf=a
else:
    hcf=b

while True:
    if a%hcf==0 and b%hcf==0:
        print("the value of hcf: ",hcf)
    hcf=hcf-1
