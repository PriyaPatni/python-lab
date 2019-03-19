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
            self.salary=input("enter again")
    def  show(self):
        print("First Name = ",self.firstname)
        print("Second Name = ", self.lastname)
        print("Salary = ", self.salary)
    def rais(self):
        self.salary=self.salary+self.salary/10
e1=employee()
e2=employee()
n=input("enter first name for e1 ")
l=input("enter last name for e1 ")
s=int(input("enter salary for e1 "))
e1.get(n,l,s)
n=input("enter first name for e2 ")
l=input("enter last name for e2 ")
s=int(input("enter salary for e2 "))
e2.get(n,l,s)
e1.show()
e2.show()
print("After 10% raise")
e1.rais()
e2.rais()
e1.show()
e2.show()


