'''
Docstring for 00_Projects.Bikerental_Project-03
1.Display available Bikes
2.Request a bike for rent(100 Rs ------>1 Qty)
3.Exit
'''


class bikeshop:
    def __init__(self,stock):    
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentBike(self,quantity):
        
        if quantity<=0:
            print("Enter the positive value or greater than zero")
        elif quantity>self.stock:
            print("Enter the value (less than stock)")
            
        else:
            self.stock=self.stock-quantity
            print("Total prices",quantity*100)
            print("Remaining Total Bikes",self.stock)
            
obj = bikeshop(100)

while True:
 userChoice=int(input('''
    1.Displpay stocks
    2.Rent a Bike
    3.Exit
    '''))   
 if userChoice==1:
     obj.displayBike()
 elif userChoice==2:
     n=int(input("Enter the Qty:----")) 
     obj.rentBike(n)
 else:
     print("Thank you for visiting")
     break
                
                         