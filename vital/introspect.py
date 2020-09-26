class user():
    def __init__(self,email):
        self.email=email
    def sign_in(self):
        print("logged in")
class wizard(user):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name=name
        self.power=power
    def attack(self):
        print(f'wizard attack with power{self.power}')
wizard1=wizard("joy",50,"sanjoysarkar.ece.@gmail.com")
#introspection of object
print(dir(wizard1))