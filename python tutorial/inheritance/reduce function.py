from functools import reduce
my_list=[1,2,3]
def Accumulator(acc,my_list):
    print(acc,my_list)
    return acc+my_list
print(reduce(Accumulator,my_list,0))
print(reduce(Accumulator,my_list,10))
#here acc is acc=0 and acc=10 to sum the list value
