class stack:
    def __init__(self):
        self.element=[]
    def isempty(self):
        return self.element==[]
    def push(self,value):
        return self.element.append(value)
    def pop(self):
        return self.element.pop()
s=stack()
if (s.isempty()==True):
    print("stack is empty")
else:
    print("stack is not empty")
s.push(10)
s.push(11)
s.push(6)
s.push(8)
s.push(9)
s.push(4)
print(s.element)
print("poped element=",s.pop())
print(s.element)
if (s.isempty()==True):
    print("stack is empty")
else:
    print("stack is not empty")
