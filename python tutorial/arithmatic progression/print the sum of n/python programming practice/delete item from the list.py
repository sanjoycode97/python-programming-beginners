My_list=[1,2,3,4,5,6,7]
delete=int(input("enter the item you want to delete: "))
count=0
sum=0
for x in My_list:
    if delete == x:
        count=count+1
    sum=sum+x
if count==0:
    print("the number is not in the list")
else:
    print("the number is successfully deleted")
    My_list.remove(delete)
    print(My_list)
print(sum)