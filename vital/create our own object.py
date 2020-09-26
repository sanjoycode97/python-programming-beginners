#create a small gaming programming
class PlayerCharacter:
    def __init__(self, name, age):
        self.name=name#attributes
        self.age=age
    def run(self):
        print('run')#when a function doesnt return anything its return none
        return "done"
player1=PlayerCharacter('cindy',25)#we are passing the argument
player2=PlayerCharacter('joy',22)
player2.attack=50
print(player1.run())#here we acces the attribute
print(player2.attack)