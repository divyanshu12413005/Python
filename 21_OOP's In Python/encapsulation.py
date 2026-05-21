class student:
    __name="Ravi"
    def __init__(self):
        print(self.__name)
        
        self.__displayinfo()
    
    def __displayinfo(self):
        print("Hello World!")   

obj=student()         