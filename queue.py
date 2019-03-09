class QUEUE:
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def enqueue(self,value):
        return self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
q=QUEUE()
if (q.isempty()==True):
    print("queue is empty")
else:
    print("queue is not empty")
q.enqueue(10)
q.enqueue(11)
q.enqueue(6)
q.enqueue(8)
q.enqueue(9)
q.enqueue(4)
print(q.queue)
print("dequeue=",q.dequeue())
print(q.queue)
if (q.isempty()==True):
    print("queue is empty")
else:
    print("queue is not empty")
