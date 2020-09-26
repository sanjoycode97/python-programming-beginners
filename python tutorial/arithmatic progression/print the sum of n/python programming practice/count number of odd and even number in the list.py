My_list=[1,2,3,4,5,6,7,8]
even=0
odd=0
for x in My_list:
    if x%2==0:
        even=even+1
    else:
        odd=odd+1
print(" ",even)
print(" ",odd)