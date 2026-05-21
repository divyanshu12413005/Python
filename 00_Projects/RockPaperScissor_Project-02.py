import random
l=['Rock','Paper','Scissor']

while True:
    
    usercount=0
    computercount=0    
    userChoice=int(input('''
                         Game start......
                         1.YES
                         2.NO|EXIT
                         '''))
    if userChoice==1:
        for a in range (1,6):
            userInput=int(input('''Enter your choice:
                                   1.Rock
                                   2.Paper 
                                   3.Scissor 
                                   '''))
            if userInput==1:
                userInput='Rock'
            elif userInput==2:
                userInput='Paper'   
            elif userInput==3:
                userInput='Scissor'
            else:
                print("Invalid Input! Please enter a valid choice.")
                continue    
            ComputerChoice=random.choice(l)
            if userInput==ComputerChoice:
                print("Computer choice is:",ComputerChoice)
                print("User choice is:",userInput)
                print("It's a Tie!")    
                usercount+=1
                computercount+=1
            elif (userInput=='Rock' and ComputerChoice=='Scissor') or (userInput=='Paper' and ComputerChoice=='Rock') or (userInput=='Scissor' and ComputerChoice=='Paper'):
                print("Computer choice is:",ComputerChoice)
                print("User choice is:",userInput)
                print("You Win!")
                usercount+=1
                
                
            else:
                print("Computer choice is:",ComputerChoice)
                print("User choice is:",userInput)
                print("You Lose!")
                computercount+=1
        print("User Score is:",usercount)
        print("Computer Score is:",computercount)
        if usercount>computercount:
            print("Congratulations! You won the game.")
        elif usercount<computercount:
            print("Sorry! You lost the game.")
            
        else:
            print("The game is a Tie!")    
            
            
    else:
        break
    
  




