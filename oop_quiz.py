class Electronic_device:
    divisor_rule = 5
    rank = 5
    def isrank(self):
        return f"Your rank {self.rank} for electronic device in market"
    @classmethod
    def change_rule(cls,new_rule):
        cls.divisor_rule=new_rule


class Pocket_gadget(Electronic_device):
    divisor_rule=10
    rank = 7
    def isrank(self):  
        return f"Your rank {self.rank} for pocket gadget in market"
  
class Phone(Pocket_gadget):
    divisor_rule=12
    rank = 10
    def isrank(self):
        return f"Your rank {self.rank} for phone in market "

    
        



electronic=Electronic_device()
pocket=Pocket_gadget()
phone=Phone()

Electronic_device.change_rule(33)
# Pocket_gadget.change_rule(111)
# Phone.change_rule(222)
print(phone.divisor_rule)
print(pocket.divisor_rule)
print(electronic.divisor_rule)

# print(electronic.isrank())
# print(pocket.isrank())
# print(phone.isrank())








input()
