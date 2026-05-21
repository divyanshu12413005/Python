class A:
    def displayA(self):
      print("This is A")
      
class B(A):
    def displayB(self):
        print("This is B")  
         
 # this is multi level inheritance       
class C(B):
    def displayC(self):
        print("This is C")
         
    
      
obj=C() 
obj.displayA()     
obj.displayB()  
obj.displayC()