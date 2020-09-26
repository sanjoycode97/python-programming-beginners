from array import *
student=array("i",[])
n=int(input("range of the array:" ))
for x in range(n):
    element=int(input("enter the elements: "))
    student.append(element)
student1=array("i",[])
for x in student:
    if x not in student1:
        student1.append(x)
print(student1)