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

# emp1.email='This.that@gmail.com'
# print(emp1.email)

del emp1.email
print(emp1.email)
emp1.email='Harry.Haider@gmail.com'
print(emp1.email)

input()