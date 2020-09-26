#abstraction is the proccess of hiding the information
class PlayersCharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print(f'my name is {self.name},and my age is {self.age}')
player1=PlayersCharacter("joy",22)
player1.speak()#we can use speak we dont need to look how speak is implemented the information is hide this is call abstractiion
