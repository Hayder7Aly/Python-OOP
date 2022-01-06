class Dad:
    basket=2

    dance=2
    def isdance(self):
        return f"Yes i dance {self.dance} times only "
    

class Son(Dad):
    dance=4
    def isdance(self):
        return f"Yes i dance {self.dance} times"


class Grandson(Son):
    dance=6
    # def isdance(self):
    #     return f"Jackson yeah I dance Awsomely {self.dance} times only"


darry=Dad()
larry=Son()
carry=Grandson()

print(carry.isdance())

# print(darry.isdance())
# print(larry.isdance())
# print(carry.isdance())
input()