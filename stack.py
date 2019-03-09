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
print(s.isempty())
s.push(10)
s.push(11)
s.push(6)
s.push(8)
s.push(9)
s.push(4)
print(s.element)
print(s.pop())
print(s.isempty())
