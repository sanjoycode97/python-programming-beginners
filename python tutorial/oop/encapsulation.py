#encapsulation is the process of binding data and methods and function that manupulate the data
class PlayersCharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        '''
          def speak(self):
        print(f'my name is {self.name},and my age is {self.age}')
player1=PlayersCharacter("joy",22)
player1.speak()
'''
player1=PlayersCharacter("joy",22)
print(player1.name)
print(player1.age)
player2={"name": "joy","age": 22}
print(player2["name"])
print(player2["age"])