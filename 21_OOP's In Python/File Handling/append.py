file=open("demofile.text","a")                                 #a i.e append it add new data without removing previous data where as w i.e write it add new data only it does not add prevoius data
file.writelines("hello ji\n""Hello World!\n""Rampal")
file.close()


with open("demofile.text", "r") as file:  
    print(file.read())

    

  
  
    
    