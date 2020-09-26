
def passwordchek():
    username = input("enter your user name: ")
    password = input("enter your password: ")
    lengthofpassword = len(password)
    hiddenpassword = "*" * lengthofpassword
    return (f'user name is {username} and password is {hiddenpassword}')
ps1=passwordchek()
print(ps1)