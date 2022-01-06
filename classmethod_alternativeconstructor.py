class Employee:
    no_of_leaves = 8
    salary=5000
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def printdetails(self):
        return f"Name is : {self.name}\nAge is  : {self.age}\nRole is : {self.std}"
    @classmethod # TODO NOTE : Class method change class atribute
    def change_leave(cls,new_leaves,new_slaray):
        cls.no_of_leaves=new_leaves
        cls.salary=new_slaray
       
    @classmethod
    def from_str(cls,string):
        # params=string.split('-') #TODO params varaible is change in list :
        # return cls(params[0] ,params [1], params [2])
        return cls(*string.split('-')) # TODO one linear fuction with args
    @classmethod
    def from_slash(cls,string):
        return cls(*string.split('/'))


        
haider = Employee('Haider',15,'student')

harry  = Employee('Harry',22,'Instructor')

ali =  Employee.from_str('Ali-19-student')

farman=  Employee.from_slash('Farman/21/student')

print(farman.age)

print(ali.std)


haider.change_leave(5,1000)


# print(harry.salary)
# print(haider.salary)

input()