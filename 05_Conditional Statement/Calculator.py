num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
op=input("Enter operator (+,-,*,/): ")
if op=='+':
    print("Addition:",num1+num2)
elif op=='-':
    print("Subtraction:",num1-num2)
elif op=='*':
    print("Multiplication:",num1*num2)
elif op=='/':
    if num2!=0:
        print("Division:",num1/num2)
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid operator")
        
      