email=input("Enter your email:----")  #g@g.in  at least 5 character contain email
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):         #.com or .in
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1  
                    elif i.isdigit():
                        continue
                    elif i=="." or i=="@" or i=="_":
                        continue 
                    else:
                        d=1       
                if k==1 or j==1 or d==1:
                    print("Wrong!!! because your email contain either one of mistake space,upper alphabet or any sign rather than @,.,or_") 
                else:
                    print("You entered correct email.")           
                    
            else:
                print("Wrong!!! dot'.' must be at last 4th placed or at 3rd placed")
        else:
            print("Wrong!!! email contain only one @")
    else:
        print(" Wrong!!! First letter of email must be alphabetic!")
else:
    print("You entered wrong email!!!!!")
    
    
    
    
    
''' or validate by using regex:-Regex is used to:-Validate email, phone number, password

-->Search text

-->Replace text

-->Filter data'''   

# import re

# email = input("Enter email: ")

# pattern = r"^[a-z][a-z0-9._]*@[a-z]+\.(com|in)$"

# if re.match(pattern, email):
#     print("Valid email")
# else:
#     print("Invalid email")

