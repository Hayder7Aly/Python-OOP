class Employee:
    leaves=8      # public variable is used in child class and other environment
    _protect = 9   # Protected variable is used in child and subclasses and do not acces in other env
    __private = 10 
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"Name : {self.name}\nAge : {self.salary}\nRole : {self.role}"
    @classmethod
    def no_of_leaves(cls,new_leaves):
        cls.leaves=new_leaves
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
    pass  


haider=Employee.from_dash('Haider-233-Programmer')
harry=Programmer.from_dash('Harry-3333-Instructor')

print(harry._protect)

print(haider.leaves)
print(haider._protect)
print(haider._Employee__private)  # TODO this is name mangly to access the private variable






input()