class user():
    def sign_in(self):
        print("you are logged in")
class wizard(user):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attackingpower(self):
        print(f'attacking power{self.power}')
class archer(user):
    def __init__(self,name,arrows):
        self.name=name
        self.arrows=arrows
    def chekarcher(self):
        print(f'archer left{self.arrows}')
    def run(self):
        print(f'run good')
class brinbog(wizard,archer):
    def __init__(self,name,power,arrows):
        wizard.__init__(self,name,power)
        archer.__init__(self,name,arrows)
bh1=brinbog("joy",50,100)
bh1.chekarcher()
bh1.sign_in()
bh1.attackingpower()
bh1.run()
