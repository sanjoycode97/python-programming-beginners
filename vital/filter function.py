my_list=[1,2,3]
def only_odd(my_list):
    return my_list%2!=0
print(list(filter(only_odd,my_list)))