class user():
    def logging(self):
     print("logged in")
class wizard(user):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'attacking power {self.power}')
class archer(user):
    def __init__(self, name,arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attacking arrows {self.arrows}')
wizerd1=wizard("rahul",50)
archer1=archer("rale",100)
wizerd1.attack()
archer1.attack()
wizerd1.logging()
archer1.logging()
#here we gonna chek is wizerd1 object instance o0f wizard class and as well as of super class user
print(isinstance(wizerd1,wizard))
print(isinstance(wizerd1,user))
print(isinstance(wizerd1,object))