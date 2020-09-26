My_list=[];
n=int(input("enter the range for the list: "))
for x in range(1,n+1):
    element=int(input("enter the element: "))
    My_list.append(element)
print(My_list)
search=int(input("enter the number you want to search: "))
if search in My_list:
    print("it is in the list")
else:
    print("not in the list")