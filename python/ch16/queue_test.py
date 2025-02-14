# queue=[1,2,3]
# queue.append(4)
# queue.pop(0)

class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return
    def is_empty(self):
        if len(self.queue)==0:
            return True
        return False
    def status_queue(self):
        return self.queue
q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.dequeue()
print(q1.status_queue())