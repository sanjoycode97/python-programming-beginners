My_list=[1,2,3,4,5,6]
delete=int(input("enter the delete item: "))
My_list.remove(delete)
print(My_list)
if delete not in My_list:
    print("not exist in the list")