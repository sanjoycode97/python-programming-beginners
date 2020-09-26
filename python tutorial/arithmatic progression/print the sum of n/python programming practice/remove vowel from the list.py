My_list=["l","m","n","a","i","U","E"]
Vowel_list1=["a","A","e","E","i","T","o","O","u","U"]



New_list=[]
for x in My_list:
    if x not in Vowel_list1:
        New_list.append(x)
print(New_list)
