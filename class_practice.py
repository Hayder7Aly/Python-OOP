class Employee:
    leave=3
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))
    @classmethod
    def new_leaves(cls,update_leave):
        cls.leave=update_leave
    @staticmethod
    def good(how):
        return f"This is good {how}"

haider=Employee.from_dash('Haider-15-9th')
ali=Employee.from_dash('Ali-19-BSC')
# print(Employee.leave)
# Employee.new_leaves(10)
# print(Employee.leave)
print(haider.good(ali.std))

input()