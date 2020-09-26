class Playercharacter:
    @classmethod
    def adding_things(cls,num1,num2):
        return num1+num2
    @staticmethod
    def adding_things2(num1,num2):
        return num1+num2
print(Playercharacter.adding_things(2,3))
player=Playercharacter()
print(player.adding_things2(2,3))

