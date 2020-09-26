#find the duplicate in the list
li=[1,2,3,4,5,5,5]
def duplicate(li):
    duplicatelist=[]
    for items in li:
        if li.count(items)>1:
            if items not in duplicatelist:
             duplicatelist.append(items)
    return (duplicatelist)








print(duplicate(li))
