vowel_list=["A","a","e","E","i","I","o","O","u","U"]
s1=input("enter the string: ")
s2=input("enter the string: ")
s3=input("enter the string: ")
s=""
for i in s1:
    if i in vowel_list:
        s1=s1.replace(i,"$")
for x in s2:
    if x not in vowel_list:
        s2=s2.replace(x,"#")
for y in s3:
    if y.isupper()==True:
        s=s+y.lower()
    else:

        s=s+y.upper()



print(s1+s2)
My_list=[]
My_list.append(s1)
My_list.append(s2)
My_list.append(s)
x=''.join(My_list)
print(x)