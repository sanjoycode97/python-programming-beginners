class highest:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2 = dim2

    def largestnumber(self):
        if self.dim1>self.dim2:
            return "first is big"
        return "second id big"
dim1=int(input("enter the first number : "))
dim2=int(input("enter the second number : "))
first=highest(dim1,dim2)
print(first.largestnumber())
dim3=int(input("enter the first number : "))
dim4=int(input("enter the first number : "))
second=highest(dim3,dim4)
print(second.largestnumber())
