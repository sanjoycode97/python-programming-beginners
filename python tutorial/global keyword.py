total=0
def count():
    global total
    total=total+1
    return total

count()
count()
count()
print(count())



total=0
def count(total):

    total=total+1
    return total


print(count(count(count(total))))