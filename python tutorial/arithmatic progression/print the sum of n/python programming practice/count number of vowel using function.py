s1=input("enter the string: ")
def count_vowel(s1):
    list=["a","A","e","E","i","I","o","O","u","U"]
    count=0
    for x in s1:
        if x in list:
            count=count+1
    return count
vowel=count_vowel(s1)
print(vowel)