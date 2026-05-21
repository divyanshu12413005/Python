class A:
    def showdata(self):
        print("I'm in A!")
class B(A):
    def showdata(self):
        super().showdata()     
        print("I'm in B!")    

obj=B()
obj.showdata()            