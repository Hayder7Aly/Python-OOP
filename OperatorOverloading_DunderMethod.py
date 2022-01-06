class Employee:
    no_of_leaves=3
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def print_details(self):
        return f"Name {self.name}\nSalary {self.salary}\nRole {self.role}\nLeaves {self.no_of_leaves}"
    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

    def __add__(a,b):
        return a.salary+b.salary
    def __truediv__(self,other):
        return self.salary/other.salary
    def __floordiv__(self,other):
        return self.salary//other.salary
    def __and__(self,other):
        return self.salary & other.salary
    def __xor__(self,other):
        return self.salary^other.salary
    def __pow__(self,other):
        return self.salary**other.salary
    def __mul__(self,other):
        return self.salary*other.salary
    def __mod__(self,other):
        return self.salary%other.salary
    def __mod__(self,other):
        return self.salary%other.salary
    def __rshift__(self,other):
        return self.salary>>other.salary
    def __repr__(self):
        return f"Employee ('{self.name} , {self.salary} , '{self.role}' , {self.no_of_leaves})"
    def __str__(self):
        return self.print_details()

emp1=Employee('Haider',46,'Student')
emp2=Employee('Ali',2,'Instructor')
emp3=Employee('farman',33,'Construcotr')


print(emp1) # TODO str is default function.
# print(repr(emp2))
# print(emp1)
# print(emp1 >> emp2)

# add=emp1.salary + emp2.salary + emp3.salary
# print(add)

# print(emp1 + emp2)



# print(emp1 + emp2 )

# emp1.change_leaves(33)
# print(emp2.no_of_leaves)
# print(emp1.print_details())

input()