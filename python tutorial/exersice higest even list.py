#print the higest even number list  from the list
def even_highest(li):
    highest_even=[]
    for items in li:#first have to ireted the list to store the list value in the items variable
        if items%2==0:#check the condition for even
            highest_even.append(items)#even number gulo store hochhhe
    return(max(highest_even))#tader mddhy max number ta k return korbe
s1=even_highest([2,3,4,5,10])
print(s1)
