class A:
    def met(self):
        print('This fuction run from class A')
class B(A):
    def met(self):
        print('This fuction run from class B')
class C(A):    
    def met(self):
        print('This fuction run from class C')
class D(C,B):
    def met(self):
        print('This fuction run from class D')
   
a=A()
b=B()
c=C()
d=D()

a.met()
b.met()
c.met()
d.met()

input()