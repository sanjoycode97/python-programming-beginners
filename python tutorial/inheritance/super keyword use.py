class user(object):
    def __init__(self,email):
        self.email=email
    def sign_in(self):
        print("logged in")
class wizard(user):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name=name
        self.power=power
        self.email=email
    def attack(self):
        print(f'he attack with{self.power}')
wizard1=wizard("joy",50,"sanjoy sarkar@")
print(wizard1.email)