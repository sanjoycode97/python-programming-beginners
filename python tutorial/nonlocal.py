def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner : ",x)#inner function er vetore print korlm x variable k
    inner()#sei function er baire ase function ta k call dilm
    print("outer : ",x)#outer function er vetore variable ta k print korlm
outer()#outer function er baire outer function ta k call krlm