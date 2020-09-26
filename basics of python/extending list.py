class superlist(list):
    def __len__(self):
        return 1000
superlist1=superlist()
print(superlist1.__len__())
print(len(superlist1))
#if we want to extend the list so we have to create a new super class of super class here list is superclass of superclass
#here we can append item in superclass of superclass which is list
superlist1.append(5)
superlist1.append(6)

print(superlist1[0])
print(superlist1[1])