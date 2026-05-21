class A:
    def displayA(self):
      print("This is A")
      
class B:
    def displayB(self):
        print("This is B")  
         
 # this is multi level inheritance       
class C(A,B):
    def displayC(self):
        print("This is C")
         
    
      
obj=C() 
obj.displayA()     
obj.displayB()  
obj.displayC()