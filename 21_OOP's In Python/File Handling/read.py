with open("demo.text","r") as file:
    print(file.read())
    file.seek(0)
    print(file.readline())   #it works line wise 
    file.seek(0)             #seek(O) gives  us positions
    

    print(file.read(5))  #read first ficve letters
    print(file.tell())   #tell gives us current position 
    print(file.readline())  #read remaining letters in firts line 
    file.seek(0)
   
    
    
    list=file.readlines()   #readlines convert into list
    print(list)
    
