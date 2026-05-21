class student:
    def displayinfo(self):
        print("Welcome student")
    
class teacher(student):
    def displayinfo(self):
        super().displayinfo()             # super keyword is use beacuse it dispaly the output of welcome student
        print("Welcome Teacher")        
        
obj=teacher()
obj.displayinfo()   