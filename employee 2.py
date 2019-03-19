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
    def rais(self):
        self.salary=self.salary+self.salary/10
e1=employee()
e2=employee()
e1.get("Priya","Patni",5000.00)
e1.show()
e2.get("xyz","abc",3000.00)
e2.show()
print("After 10% raise")
e1.rais()
e2.rais()
e1.show()
e2.show()


