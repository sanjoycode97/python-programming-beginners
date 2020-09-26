n=input("enter the number: ")

diff=0
diff1=0
for x in range(0,len(n)):
    if x%2==0:
        diff=diff+int(n[x])
    else:
        diff1=diff1+int(n[x])
print(abs(diff-diff1))
