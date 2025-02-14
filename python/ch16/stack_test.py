# stack=[]
# stack=[1,2,3]
# stack.append(4)
# print(stack)

# stack=[1,2,3]
# stack.pop()
# print(stack)

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return
    def is_empty(self):
        if len(self.stack)==0:
            return True
        return False
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return
    def status_stack(self):
        return self.stack
    
s1=Stack()
s1.push(4)
s1.push(5)
s1.pop()
print(s1.status_stack())
        