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
n=input("enter first name ")
l=input("enter last name ")
s=int(input("enter salary "))
e.get(n,l,s)
e.show()
n=input("enter first name ")
l=input("enter last name ")
s=int(input("enter salary "))
e.get(n,l,s)
e.show()
