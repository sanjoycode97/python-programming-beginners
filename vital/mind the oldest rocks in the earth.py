#find the oldest rock in the earth using the class method
#initiate the rock object with 3 rocks
#create the function what finds the oldest rock
#print out the oldest rock.exmple is the rock is x years old which is the age of rock
class rock:
    object="rock"
    def __init__(self,age):
        self.age=age

def Oldest_rock(*args):
        return max(args)
rock1=rock(5)
rock2=rock(6)
rock3=rock(7)

print(f"the oldest rock is {Oldest_rock(rock1.age,rock2.age,rock3.age)}years old")