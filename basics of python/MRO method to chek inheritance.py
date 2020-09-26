class x:
    pass
class y:
    pass
class z:
    pass
class A(x,y):
    pass
class B(y,z):
    pass
class M(B,A,z):
    pass
print(M.__mro__)