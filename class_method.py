class Employee:
    no_of_leaves = 9
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def printdetails(self):
        return f"Name is : {self.name}\nAge is  : {self.age}\nRole is : {self.std}"
    @classmethod
    def change_leave(cls,new_leaves):
        cls.no_of_leaves=new_leaves
        # cls.self.age=age1




        
haider = Employee('Haider',15,'student')

harry  = Employee('Harry',22,'Instructor')

print(harry.printdetails(),'\n')

print(haider.printdetails())

# Employee.no_of_leaves=15+2
haider.no_of_leaves=15+2

# print(Employee.no_of_leaves)

haider.change_leave(34)

print(haider.no_of_leaves)


# Employee.no_of_leaves=22
Employee.change_leave(23)
print(Employee.no_of_leaves)




input()