class A:
    def __init__(self,e):
        self.e=e;
    def get(self):
        self.x=self.e.split('@')
    def show(self):
        print("username-",self.x[0])
        print("domain-",self.x[1])
a=input("enter email id:-")
obj=A(a)
obj.get()
obj.show()


