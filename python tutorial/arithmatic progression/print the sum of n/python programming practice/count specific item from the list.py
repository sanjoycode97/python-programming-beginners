My_list=[1,2,3,4,5,5,5]
item=1
def count_specific_item(My_list,item):
    count=0
    for x in My_list:
        if x==item:
            count=count+1
    return count
    if count==0:
        return 0
chek=count_specific_item(My_list,item)
print(chek)
