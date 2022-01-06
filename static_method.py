class Employee:
    no_of_leaves = 8
    salary=5000
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def printdetails(self):
        return f"Name is : {self.name}\nAge is  : {self.age}\nRole is : {self.std}"
    @classmethod
    def change_leave(cls,new_leaves,new_slaray):
        cls.no_of_leaves=new_leaves
        cls.salary=new_slaray
       
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

    @classmethod
    def from_slash(cls,string):
        return cls(*string.split('/'))

    @staticmethod
    def print_code(string):
        return f'This is good {string}'

        
haider = Employee('Haider',15,'student')

harry  = Employee('Harry',22,'Instructor')

ali =  Employee.from_dash('Ali-19-student')

farman=  Employee.from_slash('Farman/21/student')

print(haider.print_code('Haider Ali '))

input()


