#square
my_list=[1,2,3]
print(list(map(lambda x: x*x,my_list)))
#list sorting
a=[(0,2),(4,3),(9,9),(10,-9)]
#sorting the list of tuples
a.sort()
print(a)
#sort in reverse way list of tuples
a.sort(reverse=True)
print(a)
#sort according to critera using lambda function
a.sort(key=lambda x: x[1])
print(a)#here we use the sorting according to second index(1) position sorting
#it will sort according the second index position of each tuples in the list
#if we sort the list of tuples accordind to their index value in reverse order
a.sort(key=lambda x: x[1],reverse=True)
print(a)