class Queue:
    
    def __init__(self):
        self.list = []
        
    def Dequeue(self):
        if len(self.list) > 0:
            first = self.list[-1]
            del self.list[-1]
            return first
    
    def Enqueue(self,val):
        self.list.insert(0,val)
        return val

cola1 = Queue()
print(cola1.Enqueue(1))
print(cola1.Enqueue(2))
print(cola1.Enqueue(3))

print(cola1.Dequeue())
print(cola1.Dequeue())
print(cola1.Dequeue())
print(cola1.Dequeue())


        