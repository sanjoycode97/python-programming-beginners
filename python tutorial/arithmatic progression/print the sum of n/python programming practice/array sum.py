from array import *
arr=array("i",[1,2,3,4,5])
value=5
class Array:
 def __init__(self,arr,value):
     self.arr=arr
     self.value=value
 def sum_Array(self):
  sum=0


  for x in self.arr:

    sum=sum+x

  print(sum)
 def check_value(self):
     count = 0

     for x in self.arr:
         if self.value == x:
             count = count + 1
     if count == 0:
         print("not in the array")
     else:
         print("yes in the array")
sum=Array(arr,value)
sum.sum_Array()
sum.check_value()