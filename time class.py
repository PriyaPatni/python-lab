class Time:
    def __init__(self):
        self.h=12
        self.m=00
        self.s=00
    def gettime(self,h,m,s):
          self.h=h
          self.m=m
          self.s=s
    def showtime(self):
        print("Time =",self.h,":",self.m,":",self.s)
t=Time()
t.showtime()
t.gettime(4,20,30)
t.showtime()
