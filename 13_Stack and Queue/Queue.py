l=[]
while True:
    c=int(input('''
                1. Enqueue element
                2. Dequeue element
                3. Front element
                4. Rear element   
                5. Display queue
                6. Exit
                '''))   
    if c==1:
        n=int(input("Enter the element to be Enqueue: "))
        l.append(n)
        print(l)
        
    elif c==2:
        if len(l)==0:
            print("Queue is empty, cannot Dequeue element")
        else:
            p=l.pop(0)
            print("Popped element is: ",p)
            print(l)
    
    elif c==3:
        if len(l)==0:
            print("Queue is empty")
        else:
            print("Front element is: ",l[-1])
    
    elif c==4:
        if len(l)==0:
            print("Queue is empty")
        else:
            print("Rear element is: ",l[0])
    
    elif c==5:
        print("Queue elements are: ",l)
    
    elif c==6:
        break    
    else:
        print("Invalid choice, please try again")                    