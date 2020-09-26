class user():
    def logging(self):
     print("logged in")
    def attack(self):
        print("nothing")
class wizard(user):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'attacking power {self.power}')
        user.attack(self)
class archer(user):
    def __init__(self, name,arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attacking arrows {self.arrows}')
wizerd1=wizard("rahul",50)
archer1=archer("rale",100)
def many_form(char):
    char.attack()
    char.logging()
many_form(wizerd1)
many_form(archer1)
for char in [wizerd1,archer1]:
    char.attack()
    char.logging()
