class Employee:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
    def print_details(self):
        return f"Name : {self.name}\nAge : {self.age}\nRole : {self.role}"

name1=input('\tEnter  Your  Name :')
age1=input('\tEnter  Your  Age :')
role1=input('\tEnter  Your  Role :')


user1=Employee(name1,age1,role1)
print(user1.print_details())

input()

