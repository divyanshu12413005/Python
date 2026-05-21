age=eval(input("Tell your age:--"))

if age<10 or age>18:
    raise ValueError("Your age must be between 10 and 18")
else:
    print("Welcome to club")
print("The club will start soon")    
                