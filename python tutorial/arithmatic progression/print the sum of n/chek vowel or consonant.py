ch=input("enter the character: ")
def chekvowel(ch):
 lvowel=["a","e","i","o","u"]
 uvowel=["A","E","I","O","U"]

 if(ch in lvowel) or (ch in uvowel):
    return "vowel"
 else:
     return "consonant"
cheking=chekvowel(ch)
print(cheking)