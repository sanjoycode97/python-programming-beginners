class Calculatearea:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    def areaoftriangle(self):
        area=0.5*self.dim1*self.dim2
        print("area: ",area)#we can use return area
    def areaofrectangle(self):
        area=self.dim1*self.dim2
        print("area",area)
dim1=int(input("enter the first value : "))
dim2=int(input("enter the secnd value : "))

t1=Calculatearea(dim1,dim2)
t1.areaoftriangle()#then we have to print(t1.area())
r1=Calculatearea(dim1,dim2)
r1.areaofrectangle()