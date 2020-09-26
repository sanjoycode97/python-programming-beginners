pattern=[
    [1,1,1,1,1],
    [1,1,1,0,0],
    [1,1,0,0,0],
    [1,0,0,0,0]
]
fill="*"
empty=" "
for row in pattern:
    for col in row:
        if col:#or we can use like this if col==1
            print(fill,end=" ")
        else:
            print(empty,end=" ")
    print()#need a new line after every rows
