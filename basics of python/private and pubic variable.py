#____is indicate the variable and method is private we cannot overwrite it
class PlayersCharacter:
    def __init__(self,name,age):
        self._name=name#this mean it is private variable we shouldent touch this
        self._age=age

    def speak(self):
        print(f'my name is {self._name},and my age is {self._age}')
player1=PlayersCharacter("joy",22)
player1.name="!!!!"
player1.speak="boooo"
print(player1.speak)
