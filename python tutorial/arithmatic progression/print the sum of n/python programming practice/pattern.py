space=0
star=5
for i in range(1,6):
    for j in range(1,space+1):
        print(" ",end=" ")
    for k in range(1,star+1):
        print("*",end=" ")
    space=space+1
    star=star-1
    print()