class Employee:
    var=1
    leaves=8
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


class Player:
    var=2
    games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def print_game_details (self):
        return f"Your Name is {self.name}\nGame is {self.game}"


class CoolProgrammer(Employee,Player):
    # We can use multiple inheritance with own programmes.
    var=4
    language=["C ",'C++']
    def print_language(self):
        print(f"Languages are {self.language}")

haider = Employee('Haider',1566,'student')
ali =  Employee.from_dash('Ali-1966-student')

harry=Player('Harry','Bedminton')

farman=CoolProgrammer.from_slash('Farman/111/cricket')


# farman=CoolProgrammer.from_slash('Farman/Cricket')
# farman.print_language()
# print(farman.printdetails())
# print(farman.print_game_details())
# print(farman.printdetails())

class CoolProgrammer(Player,Employee):
    language='Python/java'
    def print_languages(self):
        print(self.language)

harry=CoolProgrammer.from_slash('Harry/Cricket')
# print(harry.print_game_details())
harry.print_languages()
farman.print_language()

input()