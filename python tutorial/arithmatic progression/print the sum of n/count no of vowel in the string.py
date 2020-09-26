s1=input("enter the sentance")
s1=s1.lower()
list=["a","e","i","o","u"]
count=0
for x in s1:
    if x in list:
        count=count+1
print(count)