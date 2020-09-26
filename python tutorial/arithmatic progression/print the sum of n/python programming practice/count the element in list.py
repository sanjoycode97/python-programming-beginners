My_list=[1,2,3,4,5,5,5,5]
item=int(input("enter the item you want to count: "))
count=0
for x in My_list:
    if item==x:
        count=count+1
print(count)
if count==0:
    print("number is not in the list")
