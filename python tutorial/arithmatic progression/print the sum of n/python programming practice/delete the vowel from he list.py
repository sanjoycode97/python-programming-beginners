My_list=["a","b","c","d"]
vowel_list=["a","e","i","o","u"]
delete=input("enter the vowel: ")
count=0
if(delete in My_list) and (delete in vowel_list):
    count=count+1
if count==0:
    print("please enter the vowel")
else:
    print("vowel successfully deleted")
    My_list.remove(delete)
    print(My_list)