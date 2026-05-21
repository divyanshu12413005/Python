class Area:
    def findarea(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area is:",a*b)
        elif a!=None:
            print("Area is:",a*a) 
        # elif b!=None:
        #     print("Area is:",b*b)
            
        else:
            print("Nothing to find")     
obj=Area()
obj.findarea()
obj.findarea(15)
# obj.findarea(25)
obj.findarea(10,30)           