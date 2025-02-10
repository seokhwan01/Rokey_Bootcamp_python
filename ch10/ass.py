class Phone:
    def __init__(self,number,color):
        self.number=number
        self.color = color
    def showInfo(self):
        print(f"전화번호 : {self.number}")
        print(f"색상 : {self.color}")
#apple=Phone("010-9274-0795","검정")
#apple.showInfo()

class SmartPhone(Phone):
    def __init__(self,number,color,company):
        super().__init__(number,color)
        self.company = company
        
    def showInfo(self):
        print(f"전화번호 : {self.number}")
        print(f"색상 : {self.color}")
        print(f"회사 : {self.company}")
apple=SmartPhone("010-9274-0795","검정","애플")
apple.showInfo()
#print(apple.number)
#print(apple.color)
#print(apple.company)