#what variables do i have access to?
#who has access to who
#local scope which is under the local function
#parental scope which is under the parental function
#global scope out of the functions anything
if True:
    x=10#this is global scope

def parent_scope():#what intendent under parent call parent scope
 x=5

 def some_func():#what intendent under loacl call loacl scope#what we have to access from the function we have to intendent in the function
    return x
 return some_func()
print(parent_scope())
print(x)
#others is built in python