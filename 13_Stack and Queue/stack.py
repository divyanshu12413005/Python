l=[]
while True:
    c=int(input('''
                1. Push element
                2. Pop element
                3. peek element
                4. Display stack    
                5. Exit
                '''))   
    if c==1:
        n=int(input("Enter the element to be pushed: "))
        l.append(n)
        print(l)
        
    elif c==2:
        if len(l)==0:
            print("Stack is empty, cannot pop element")
        else:
            p=l.pop()
            print("Popped element is: ",p)
            print(l)
    
    elif c==3:
        if len(l)==0:
            print("Stack is empty")
        else:
            print("Top element is: ",l[-1])
    
    elif c==4:
        print("Stack elements are: ",l)
    
    elif c==5:
        break
    else:
        print("Invalid choice, please try again")                    