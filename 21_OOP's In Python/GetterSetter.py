class student:
    def __init__(self):    #this is 
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name    
        
obj=student()
obj.setname("Hello World!")  
c=obj.getname()
print(c)      
    