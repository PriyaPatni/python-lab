class employee:
    def __init__(self):
        self.firstname="xyz"
        self.lastname="abc"
        self.salary=0.0
    def get(self,fn,ln,s):
         self.firstname=fn
         self.lastname=ln
         if(s>0):
             self.salary=s
         else:
            print("Invalid salary")
            self.salary=0.0
            self.salary=input("enter again")
    def  show(self):
        print("First Name= ",self.firstname)
        print("Second Name= ", self.lastname)
        print("Salary= ", self.salary)
e=employee()
e.get("priya","patni",50000.00)
e.show()
e.get("priya","patni",-10)
e.show()
