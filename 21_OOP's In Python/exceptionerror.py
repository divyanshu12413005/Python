a=eval(input("Eneter your number:---"))

try:
    print(10/a)
# except ZeroDivisionError:  #or
except Exception as err:

    print(f"Sorry there is an error as {err}") 
else:
    print("I will run when execpt not run") 
finally:
    print("i will always run even except,else run or not") 

print("I will run in last")          
    
      