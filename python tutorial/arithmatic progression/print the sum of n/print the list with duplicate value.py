mylist=[]
for x in range(1,6):
    element=int(input("enter the element: "))
    mylist.append(element)
def find_duplicate(mylist):
    duplicate_list=[]
    for value in mylist:
        if mylist.count(value)>1:
            if value not in duplicate_list:
                duplicate_list.append(value)
    return duplicate_list
dp=find_duplicate(mylist)
print("duplicate values in list: ",dp)