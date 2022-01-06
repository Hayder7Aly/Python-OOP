class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"This email is not set . please set your fucntion"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        name=string.split('@')[0]
        self.fname=name.split('.')[0]
        self.lname=name.split('.')[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None



haider=Employee('Haider','Ali')
ali=Employee('Ali','Jutt')


# print(haider.email)

# haider.fname='farman'

# print(haider.email)


haider.email='this.that@gmail.com'

print(haider.email)

del haider.email

print(haider.email)

haider.email='Harry.perry@gmail.com'
print(haider.email)




