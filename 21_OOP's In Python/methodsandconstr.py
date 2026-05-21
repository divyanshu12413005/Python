class DemoClass:
     a = 10


     def showvalue(self):
          print(self.a)

     # parameterized method
     def addvalue(self, b, c):
          print(b + c)
          
     # making constructor
     def __init__(self):   # this is constructor
          print("This is constructor method")


obj = DemoClass()
obj.showvalue()
obj.addvalue(60, 30)
