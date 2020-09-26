from array import *
arr=array("i",[])
for x in range(5):
    element=int(input("enter the elements= "))
    arr.append(element)
value=int(input("enter the value to find= "))
class Array:
    def __init__(self,arr,value):
        self.arr=arr
        self.value=value
    def Array_sum(self):
        sum=0
        for i in self.arr:
            sum=sum+i
        print(sum)
    def check_value(self):
        count=0
        for i in self.arr:
            if value==i:
                count=count+1
        if count==0:
            print("not in the array")
        else:
            print("yes in the array")
sum=Array(arr,value)
sum.Array_sum()
sum.check_value()