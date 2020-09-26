class user:
    def sign_in(self):
        print("you are logged in")
class wizard(user):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'wizerd ,{self.name}, attacking with power{self.power}')
class archer(user):
    def __init__(self,name,arrowes):
        self.name=name
        self.arrowes=arrowes
    def attack(self):
        print(f'archer {self.name} attacking with arrowes{self.arrowes}')
wizard1=wizard("tom",50)
wizard1.attack()
archer1=archer("heiley",500)
archer1.attack()
wizard1.sign_in()
archer1.sign_in()
