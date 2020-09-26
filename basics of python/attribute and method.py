class PlayCharacter:
    #class obhect attribute which is not dynamic its static
    membership=True
    def __init__(self, name ,age):
        if self.membership:
         self.name=name#attribute
         self.age=age
    def shout(self):

        return f"my name is {self.name}"
    def run(self, r):

        return r
player1=PlayCharacter('joy',22)
player2=PlayCharacter('nandini',19)
print(player1.shout())#we can use to chek the player1.membership
print(player2.run('hello'))