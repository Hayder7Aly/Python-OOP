# Polyphorism is a consept its means we can over ride funtion in sub-class or child class
class Phone:
    rank =  10
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def print_details(self):
        return f"Phone {self.name}\tModel {self.model}\tRank {self.rank}"
class Cellphone(Phone):
    rank = 4
    def print_details(self):
        return f"Phone Name {self.name}\nModel in {self.model}\nRank is {self.rank}"


ph=Phone('Nokia','DT3Dt')
cph=Cellphone('OppO','Ye3Ye')


print(ph.print_details())
print(cph.print_details())

input()
