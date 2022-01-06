class A:
    classvar1='I am in class A variable'
    def __init__(self):
        self.var1="I am inside class variable A's construcotr"
        self.classvar1='Instance variable in class A'
        self.special='Special Variable'
        self.haider='Haider ali jutt'


class B(A):
    classvar1='I am in class B'
    var1='variable in A'
    def __init__(self):
        self.var1='I an inseide varialbe B"s construcotr'
        self.classvar1='I am in Class B instance varable'
        self.special='sp v b'
        self.haider='Haider'
        super().__init__()


a=A()
b=B()



# print(a.special)
# print(a.classvar1)
# print(a.var1)


print(b.special)
print(b.classvar1)
print(b.var1)
print(b.haider)



input()