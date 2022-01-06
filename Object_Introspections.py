# TODO object introspections means to know what type data and class name to locate from attribute and  
#functions


class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@gmail.com"
    # @property
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        print('Property now')
        if self.fname==None or self.lname==None:
            return f"Please set your email."
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        print('Setting now')
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]
    @email.deleter
    def email(self):
        print('Deleter now')
        self.fname=None
        self.lname=None


emp1=Employee('Haider','Ali')


# print(id('Int consists of collection of digit from 0-9 '))
# print(id('string is collection of character '))
dir1='this is a string'
print(dir(emp1))

# import inspect
# print(inspect.getmembers(Employee.__init__))
input()
