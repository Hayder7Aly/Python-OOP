class Employee:
    no_of_leaves = 9
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def printdetails(self):
        return f"Name is : {self.name}\nAge is  : {self.age}\nRole is : {self.std}"
haider = Employee('Haider',15,'student')


# haider.name='Haider Ali'
# haider.age=15
# haider.std='Student'


harry  = Employee('Harry',22,'Instructor')


# harry.name='Harry'
# harry.age=18
# harry.std='Instructor'

print(harry.printdetails(),'\n')

print(haider.printdetails())







input()