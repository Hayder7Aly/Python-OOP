class Employee:
    no_of_leaves = 9
    pass

haider = Employee()
haider.name='Haider Ali'
haider.age=15
haider.std='Student'
harry  = Employee()
harry.name='Harry'
harry.age=18
harry.std='Instructor'
print(Employee.no_of_leaves)
print(haider.no_of_leaves)
print(haider.__dict__)
haider.no_of_leaves=12
print(haider.__dict__)
print(Employee.__dict__)
Employee.no_of_leaves=10
print(Employee.__dict__)

input()
