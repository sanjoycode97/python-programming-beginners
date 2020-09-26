class PlayerCharacter:
    def __init__(self,name,age):
        if age>18:
         self.name=name
         self.age=age
    def start(self):
        return(f"my name is {self.name} and my age is {self.age}")
player1=PlayerCharacter("joy",22)
print(player1.start())
player2=PlayerCharacter("nandini",26)
print(player2.start())