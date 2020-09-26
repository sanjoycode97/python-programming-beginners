arr=[]
num=int(input("enter the range of input in array: "))
for x in range(num):
    element=int(input("enter the element in araay: "))
    arr.append(element)
print("Maximum value of array: ",max(arr))
print("Minmum value of array: ",min(arr))
