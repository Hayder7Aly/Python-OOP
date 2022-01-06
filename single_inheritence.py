class Employee:
    leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"Name : {self.name}\nAge : {self.salary}\nRole : {self.role}"
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))
    @classmethod
    def from_slash(cls,string):
        return cls(*string.split('/'))
    @staticmethod
    def code(string):
        return f"THIS IS GOOD {string}"

class Programmer(Employee):
    leaves=5
    def __init__(self,name,salary,role,languages):
        self.name=name
        self.salary=salary
        self.role=role
        self.languages=languages
    def print_prog(self):
        return f"THE programmer's name {self.name}\nSalary {self.salary}\nRole {self.role}\nlanguages are :{self.languages}"
      
haider = Employee('Haider',1566,'student')
ali =  Employee.from_dash('Ali-1966-student')
farman=  Programmer.from_slash('Farman/2166/student/[C , Cpp]')
harry=  Programmer.from_slash('harry/21345/student/[Python, Cpp]')

# NOTE 
# we can use both class function in programmer class TODO but employee class 
# instance not use progrmmer class function.

# print(farman.print_prog())
# print(harry.printdetails())mu
# print(ali.printdetails())
# print(haider.printdetails())



# print(harry.print_prog())
# print(harry.printdetails())
# print(haider.code('Haider Ali Jutt'))
print(haider.code(harry.languages))

print(harry.leaves)
print(haider.leaves)
print(farman.print_prog())


input()