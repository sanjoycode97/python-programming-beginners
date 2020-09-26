My_list=[]
n=int(input("enter the range for the list: "))
for x in range(1,n+1):
    element=input("enter the element: ")
    My_list.append(element)
search=input("enter the word you want to search: ")
if search in My_list:
    print("it is the list")
else:
    print("not in the list")