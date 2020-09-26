ch=input("enter the letter= ")
if (ch=='V'):
    space=4
    star=1
    space2=4
    for i in range(1,6):
        for j in range(1,space+1):
            print(" ",end=" ")
        for k in range(1,star+1):
            print("*",end=" ")
        for l in range(1,space2+1):
            print(" ",end=" ")
        space=space-1
        star=star+2
        space2=space2-1
        print()
