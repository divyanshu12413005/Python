import random
Cnumber = random.randint(1, 100)
userInput=int(input("Guess a number between 1 to 100: "))

if userInput > Cnumber:
        print("Computer Number is:",Cnumber)
        print("Too high! Try again.")
       
elif userInput < Cnumber:
        print("Computer Number is:",Cnumber)
        print("Too low! Try again.")
       
else:
        print("Congratulations! You guessed the correct number:", Cnumber)
        