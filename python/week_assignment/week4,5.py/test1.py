class Stack:
    def __init__(self,data):
        self.data=data
        
    def push(self,x):
        self.data.append(x)
        
    def show(self):
        print(self.data)
        
    def pop(self):
        if self.data:
            del self.data[0]
            
    def remove_kim(self):
        while True:
            if self.data :
                if self.data[0]=="김려은":
                    self.pop()
                    break
                else:
                    self.pop()
            else:
                break   
list=["박승휘","이용욱","김려은"]
s=Stack(list)
s.push("정석환")
s.show()
s.remove_kim()
s.show()