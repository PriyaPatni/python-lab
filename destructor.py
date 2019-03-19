class A:
    def __init__(self):
        print("constructor of class A")
    def show(self):
        print("class A")
    def __del__(self):
        print("destructor of class A")
a=A()
a.show()
del a
        
